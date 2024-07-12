#!/usr/bin/env python3
import cv2 as cv
import mediapipe as mp
import rospy
import numpy as np
import os
from std_msgs.msg import Int8, Int16MultiArray, Int32MultiArray, Float32MultiArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

astra_flag = 0
astra_data = None
time_t = 0
time_t2 = 0
time_t3 = 0
human_hand_flag = 0
hand_storage = {}
bridge = CvBridge()

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)

rospy.init_node('Hand_detection', anonymous= True)
hand = rospy.Publisher('/right_arm_fingers',Int8, queue_size=10)
log_web_pub = rospy.Publisher('/web_log_right_eye', Int16MultiArray, queue_size=10)
right_eye_frame = rospy.Publisher('/RIGHT_EYE_FRAME',Image, queue_size=10)
face = rospy.Publisher('/face_xmin', Float32MultiArray, queue_size=10)

handle_calibrate_flag = 0

box_coordinate = [0,0,0,0]

def _astra_camera_callback(data):
    # global astra_data
    global astra_flag
    
    if astra_flag == 0:
        time_t3 = 0
    else:
        pass
    
    if (rospy.get_time() - time_t3) > 1:
        if data.data[3] == 0:
            os.environ['astra_data'] = '0' # нет никого / красный
        elif data.data[3] == 1:
            os.environ['astra_data'] = '2' # кто то в жёлтом
        elif data.data[3] == 2:
            os.environ['astra_data'] = '2' # кто то в синем 


rospy.Subscriber('/astra_eyes', Int32MultiArray, _astra_camera_callback)

def robot_hand_capture():
    """
        Захватываем движение руки и головые с помощью нейронной сети
    """
    
    global handle_calibrate_flag
    global time_t
    global time_t2
    global cap
    global right_eye_frame
    global bridge
    global hand
    global face
    # global astra_data
    global astra_flag
    global log_web_pub
    global box_coordinate
    global hand_storage
    global human_hand_flag

    data_hand = Int8()
    data_face = Float32MultiArray()
    log_web_pub_data = Int16MultiArray()
                          #id cx cy
    log_web_pub_data.data = [0,0,0]
                    # flag , xmin
    data_face.data = [0  ,  0]

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    face_detection  = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)

    cx_array = []
    cy_array = []

    while True:
        success, image = cap.read()
        imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = hands.process(imageRGB)
        rospy.logwarn(os.environ['astra_data'])
        if (int(os.environ['astra_data']) == 0 or int(os.environ['astra_data']) == 1):
            data_face.data=[0.0,0.0] # Если у нас надо пожать руку - флаг лица 0 

        if results.multi_hand_landmarks and (int(os.environ['astra_data']) == 0 or int(os.environ['astra_data']) == 1):
            
            for handLms in results.multi_hand_landmarks:
                    # working with each hand
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    cx_array.append(int(cx))
                    cy_array.append(int(cy)) 

                    if handle_calibrate_flag == 0 and id == 20 and int(os.environ['astra_data']) != None:

                        cx_mean = np.min(np.array(cx_array))
                        cy_mean = np.min(np.array(cy_array))

                        box_coordinate = [int(cx_mean-25),int(cy_mean-0),int(cx_mean+60),int(cy_mean+80)]

                        hand_storage = {
                            "id_robot_hand_20":int(id),
                            "x_robot_hand_20":int(cx),
                            "y_robot_hand_20":int(cy)
                        }

                        handle_calibrate_flag = 1

                    human_hand_storage = {
                        "id_human_hand_20":int(id),
                        "x_human_hand_20":int(cx),
                        "y_human_hand_20":int(cy)
                    }

                    if cx in range(box_coordinate[0], box_coordinate[2]) and cy in range(box_coordinate[1], box_coordinate[3]):
                        if abs(human_hand_storage["y_human_hand_20"] - hand_storage["y_robot_hand_20"]) > 10:
                            data_hand.data = 1
                        else:
                            data_hand.data = 0
                    else:
                        data_hand.data = 0

                        
                if int(os.environ['astra_data']) == 0 or int(os.environ['astra_data']) == 1:
                    cv.rectangle(image,(box_coordinate[0],box_coordinate[1]),(box_coordinate[2],box_coordinate[3]),(0,255,0),3)
                    log_web_pub_data.data = [id, cx, cy]
                mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

        else:
            data_hand.data = 0
        
        if int(os.environ['astra_data']) == 2:
            success, image = cap.read()
            if not success:
                continue

            image.flags.writeable = False
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            results = face_detection.process(image)

            image.flags.writeable = True
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

            if results.detections:
                for detection in results.detections:
                    data_face.data=[1.0,detection.location_data.relative_bounding_box.xmin]
                    mp_drawing.draw_detection(image, detection)
            else:
                data_face.data=[1.0,0.0]

        _msg_img = bridge.cv2_to_imgmsg(image, "bgr8")
        right_eye_frame.publish(_msg_img)

        if int(os.environ['astra_data']) == None:
            pass
        elif int(os.environ['astra_data']) == 2:
            data_hand.data = 0

        if (rospy.get_time() - time_t) > 0.05:
            time_t = rospy.get_time()
            hand.publish(data_hand)
            face.publish(data_face)

        if (rospy.get_time() - time_t2) > 0.1:
            time_t2 = rospy.get_time()
            log_web_pub.publish(log_web_pub_data)
        
        cv.waitKey(1)

        if rospy.is_shutdown():
            break
if __name__ == "__main__":
    robot_hand_capture()
    rospy.spin()
