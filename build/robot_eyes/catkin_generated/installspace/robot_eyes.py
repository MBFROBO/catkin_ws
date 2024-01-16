#!/usr/bin/env python3
import cv2 as cv
import mediapipe as mp
import rospy

from std_msgs.msg import Int8, Int16MultiArray, Int32MultiArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
astra_data = 0
time_t = 0
time_t2 = 0
bridge = CvBridge()

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

rospy.init_node('Hand_detection', anonymous= True)
hand = rospy.Publisher('/right_arm_fingers',Int8, queue_size=10)
log_web_pub = rospy.Publisher('/web_log_right_eye', Int16MultiArray, queue_size=10)
right_eye_frame = rospy.Publisher('/RIGHT_EYE_FRAME',Image, queue_size=10)


def _astra_camera_callback(data):
    global astra_data
    if data.data[0] == 0:
        astra_data = 0
    if data.data[0] == 1:
        astra_data = 1
    

rospy.Subscriber('/astra_eyes', Int32MultiArray, _astra_camera_callback)


def robot_hand_capture():

    global time_t
    global time_t2
    global cap
    global right_eye_frame
    global bridge
    global hand
    global log_web_pub
    global astra_data


    data_hand = Int8()

    log_web_pub_data = Int16MultiArray()
    log_web_pub_data.data = [0,0,0]

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    while True:
        success, image = cap.read()
        imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        results = hands.process(imageRGB)

        if results.multi_hand_landmarks:    
            for handLms in results.multi_hand_landmarks: # working with each hand
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    log_web_pub_data.data = [id, cx, cy]
                mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
            data_hand.data = len(results.multi_hand_landmarks)
        else:
            data_hand.data = 0

        if astra_data == 0:
            pass
        elif astra_data == 1:
            data_hand.data = 0


        if (rospy.get_time() - time_t) > 1:
            time_t = rospy.get_time()
            hand.publish(data_hand)


        if (rospy.get_time() - time_t2) > 0.1:
            time_t2 = rospy.get_time()
            log_web_pub.publish(log_web_pub_data)

        _msg_img = bridge.cv2_to_imgmsg(image, "bgr8")
        right_eye_frame.publish(_msg_img)

        cv.waitKey(1)

        if rospy.is_shutdown():
            break

if __name__ == "__main__":
    robot_hand_capture()
    
    rospy.spin()