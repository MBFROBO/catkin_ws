#!/usr/bin/env python3
import rospy
from playsound import playsound
from random import randint
from std_msgs.msg import String, Int8MultiArray

rospy.init_node('text_processing')


event = rospy.Publisher('/sound_event', Int8MultiArray, queue_size=10)

DIKTANT = [
    '/home/robot/diktant.mp.3'
]

GREET_PATH = [
    '/home/robot/greet_1.mp3',
    '/home/robot/greet_2.mp3',
    '/home/robot/greet_3.mp3',
    '/home/robot/greet_4.mp3'
]

POGODA_PATH = [
    '/home/robot/pogoda.mp3'
]



MODS = [
    '/home/robot/freedom.mp3',
    '/home/robot/handshake_1.mp3',
    '/home/robot/observe.mp3'
]

MINISTERSTVO = [
    '/home/robot/minprom_menu.mp3',
    '/home/robot/minprom1.mp3',
    '/home/robot/minprom2.mp3',
    '/home/robot/minprom3.mp3',
    '/home/robot/minprom4.mp3',
    '/home/robot/minprom5.mp3',
    '/home/robot/minprom6.mp3',
    '/home/robot/minprom7.mp3',
    '/home/robot/minprom8.mp3'

]

def callback(data):
    """
        Парсинг текста с микрофона и ответные действия
    """
    global event
    global pub_audio

    event_data_array_struct = Int8MultiArray()


    event_data_array_struct.data = [
                0, # сигнал на блокировку astra
                0  # действие
    ]

    speech_array = str(data.data).split(' ')
    
    rospy.logwarn(speech_array)
    if 'сергей' in speech_array or 'серёга' in speech_array:

        if 'привет' in speech_array or 'приветствую' in speech_array:

            num_sound = randint(0,3)
            playsound(GREET_PATH[num_sound])

        if "сергей" in speech_array and "так" in speech_array and "ведь" in speech_array:
            playsound(DIKTANT[0])

        if "погода" in speech_array:

            num_sound = randint(0,len(POGODA_PATH)-1)
            playsound(POGODA_PATH[num_sound])

        if "свободный" in speech_array and "режим" in speech_array:
            playsound(MODS[0])
            
        if "руки" in speech_array and "пожмём" in speech_array:
            playsound(MODS[1])
        
        if "смотри" in speech_array and "меня" in speech_array:
            playsound(MODS[2])

        if "химическую" in speech_array and "промышленность" in speech_array and "чувашии" in speech_array:
            playsound(MINISTERSTVO[6])
        
        if "машиностроение" in speech_array and "промышленность" in speech_array and "чувашии" in speech_array:
            playsound(MINISTERSTVO[1])

        if "электрооборудования" in speech_array and "производство" in speech_array and "чувашии" in speech_array:
            playsound(MINISTERSTVO[5])

        if "мебели" in speech_array and "производство" in speech_array and "чувашии" in speech_array:
            playsound(MINISTERSTVO[2])

        if "пищевую" in speech_array and "промышленность" in speech_array and "чувашии" in speech_array:
            playsound(MINISTERSTVO[3])

        if "текстильную" in speech_array and "промышленность" in speech_array and "чувашии" in speech_array:
            playsound(MINISTERSTVO[4])

        if "автомобильную" in speech_array and "промышленность" in speech_array and "чувашии" in speech_array:
            playsound(MINISTERSTVO[7])

        if "энергетическую" in speech_array and "промышленность" in speech_array and "чувашии" in speech_array:
            playsound(MINISTERSTVO[8])

        if "промышленность" in speech_array or "промышленности" in speech_array and "чувашии" in speech_array and "энергетическую" not in speech_array and "автомобильную" not in speech_array and "текстильную" not in speech_array and "пищевую" not in speech_array and "мебели" not in speech_array and "электрооборудования" not in speech_array and "машиностроение" not in speech_array and "химическую" not in speech_array:
            playsound(MINISTERSTVO[0])

        
        

    else:
        pass

if __name__ == '__main__':
    rospy.Subscriber('mic_sound', String, callback)
    rospy.spin()
