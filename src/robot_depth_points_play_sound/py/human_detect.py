import mediapipe as mp
import cv2
import rospy

from std_msgs.msg import Int8
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node('human_detecter')
bridge = CvBridge()

cap = cv2.VideoCapture(2)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

detecter = rospy.Publisher("/human_detecter", Image, queue_size=10)
flag_publish = rospy.Publisher("/human_detecter/flags", Int8, queue_size=10)
flag_publish_data = Int8()
time_t = 0


def human_detecter():
    global cap
    global mp_drawing
    global mp_holistic
    global cTime
    global pTime
    global bridge
    global detecter
    global flag_publish
    global flag_publish_data
    global time_t

    while True:
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            ret, frame = cap.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = holistic.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION, 
            #                         mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
            #                         mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
            #                         )
            if results.right_hand_landmarks:
                mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                flag_publish_data.data = 1
            # Left Hand
            elif results.left_hand_landmarks:
                mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
                flag_publish_data.data = 1
            # Pose Detections
            elif results.pose_landmarks:
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
                flag_publish_data.data = 1
            else:
                flag_publish_data.data = 0


            if (rospy.get_time() - time_t) > 1:
                time_t = rospy.get_time()
                flag_publish.publish(flag_publish_data)


            _msg_data = bridge.cv2_to_imgmsg(image, "bgr8")
            detecter.publish(_msg_data)
            cv2.waitKey(1)
        
if __name__ == '__main__':
    human_detecter()