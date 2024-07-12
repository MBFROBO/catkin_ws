#!/usr/bin/env python3
import rospy, os

from std_msgs.msg import String, Int8MultiArray, Int32MultiArray

rospy.init_node("signal_handler")

pub = rospy.Publisher('signal', Int8MultiArray, queue_size=10)

time_t = 0
signal_astra = None
signal_text = None


def astra_callback(data):
    global signal_astra
    signal_astra = data.data[0]

def speech_callback(data):
    global signal_text
    signal_text = data.data

def main():
    global time_t
    global signal_astra
    global signal_text
    global pub

    while True:
        signal_data = Int8MultiArray()

        signal_data.data = [
            0,
            0
        ]

        if signal_text != None:

            """
                структура 
                    >>> 1 - рукопожатие
                    >>> 2 - наблюдение
                    >>> 3 - свободный режим
                    подписываемся на этот топик в human_detect.py и блокируем астра
                    в случае флага 1,2
            """

            
            if "свободный" in signal_text and "режим" in signal_text:
                signal_data.data[0] = 3
            if "руки" in signal_text and "пожмём" in signal_text:
                signal_data.data[0] = 1
            if "смотри" in signal_text and "меня" in signal_text:
                signal_data.data[0] = 2


        if signal_astra != 0:
            signal_data.data[1] = 1

        if (rospy.get_time() - time_t) > 1:
            time_t = rospy.get_time()
            pub.publish(signal_data)
        
        rospy.Subscriber('/astra_eyes', Int32MultiArray, callback=astra_callback)
        rospy.Subscriber('/mic_sound',  String, callback=speech_callback)

main()
rospy.spin()