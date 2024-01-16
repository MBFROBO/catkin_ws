import rospy
import std_msgs
from std_msgs.msg import UInt8MultiArray


time_t = 0

def callback(data):
    holls_sensor_left   = 530
    holls_sensors_right = 530

    rightArm_hollFlag = rospy.Publisher('/right_holl', UInt8MultiArray, queue_size=10)
    leftArm_hollFlag = rospy.Publisher('/left_holl', UInt8MultiArray, queue_size=10)

    Head_left_arm = data.data[0]
    Sender = data.data[1]
    right_arm_data = UInt8MultiArray()
    right_arm_data.data = [0]*5
    left_arm_data = UInt8MultiArray()
    left_arm_data.data = [0]*5

    right_finger_1 = data.data[2]  +  (data.data[3]   << 8)       # Большой
    right_finger_2 = data.data[4]  +  (data.data[5]   << 8)       # Указательный
    right_finger_3 = data.data[6]  +  (data.data[7]   << 8)       # Средний
    right_finger_4 = data.data[8]  +  (data.data[9]   << 8)       # Безымянный
    right_finger_5 = data.data[10] +  (data.data[11] << 8)     # Мезинец

    if abs(holls_sensors_right - int(right_finger_1)) > 50:
        right_arm_data.data[0] = 1
    else:
        right_arm_data.data[0] = 0

    if abs(holls_sensors_right - int(right_finger_2)) > 50:
        right_arm_data.data[1] = 1
    else:
        right_arm_data.data[1] = 0

    if abs(holls_sensors_right - int(right_finger_3)) > 50:
        right_arm_data.data[2] = 1
    else:
        right_arm_data.data[2] = 0

    if abs(holls_sensors_right - int(right_finger_4)) > 50:
        right_arm_data.data[3] = 1
    else:
        right_arm_data.data[3] = 0

    if abs(holls_sensors_right - int(right_finger_5)) > 50:
        right_arm_data.data[4] = 1
    else:
        right_arm_data.data[4] = 0

    left_finger_1 = data.data[14] + (data.data[15] << 8)       # Большой
    left_finger_2 = data.data[16] + (data.data[17] << 8)       # Указательный
    left_finger_3 = data.data[18] + (data.data[19] << 8)       # Средний
    left_finger_4 = data.data[20] + (data.data[21] << 8)       # Безымянный
    left_finger_5 = data.data[22] + (data.data[23] << 8)

    if abs(holls_sensor_left - int(left_finger_1)) > 50:

        left_arm_data.data[0] = 1
    else:
        left_arm_data.data[0] = 0

    if abs(holls_sensor_left  - int(left_finger_2)) > 50:
        left_arm_data.data[1] = 1
    else:
        left_arm_data.data[1] = 0

    if abs(holls_sensor_left  - int(left_finger_3)) > 50:
        left_arm_data.data[2] = 1
    else:
        left_arm_data.data[2] = 0

    if abs(holls_sensor_left  - int(left_finger_4)) > 50:
        left_arm_data.data[3] = 1
    else:
        left_arm_data.data[3] = 0

    if abs(holls_sensor_left  - int(left_finger_5)) > 50:
        left_arm_data.data[4] = 1
    else:
        left_arm_data.data[4] = 0


    rightArm_hollFlag.publish(right_arm_data)
    leftArm_hollFlag.publish(left_arm_data)

rospy.init_node('heandler_holl_data')
while not rospy.is_shutdown():    
    if (rospy.get_time() - time_t) >= 1000:
        time_t = rospy.get_time()
        rospy.Subscriber('holl_heandler', UInt8MultiArray, callback)

rospy.spin()
