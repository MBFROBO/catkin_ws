import rospy
from std_msgs.msg import Int8, Int32MultiArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2 as cv
import mediapipe as mp

cap1 = cv.VideoCapture(2);
cap1.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap1.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

rospy.init_node('humqan_hand_tracker', anonymous= True)
pub = rospy.Publisher('/hum_hand_tracker',Int8, queue_size=10)
img_pub = rospy.Publisher("/HAND_STREAM_TRACK", Image, queue_size=10)
time_t = 0
bridge = CvBridge()

def human_hand_capture():
    global time_t
    global cap1
    global pub
    global bridge
    global img_pub

    track_data = Int8()
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    while True:
        success, image = cap1.read()
        imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = hands.process(imageRGB)  

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks: # working with each hand
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            track_data.data = 1
        else:
            track_data.data = 0
        _msg_img = bridge.cv2_to_imgmsg(image, "bgr8")
        img_pub.publish(_msg_img)
        cv.waitKey(1)


        if (rospy.get_time() - time_t) > 1:
            time_t = rospy.get_time()
            pub.publish(track_data)
    
        if rospy.is_shutdown():
            break

if __name__ == "__main__":
    human_hand_capture()
    
    rospy.spin()