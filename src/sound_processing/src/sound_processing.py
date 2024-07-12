#!/usr/bin/env python3
import os
from pocketsphinx import LiveSpeech, get_model_path
import rospy
import time, os, dotenv, json


from pathlib import Path
from std_msgs.msg import String

PATH_HMM    = '/home/robot/Загрузки/zero_ru_cont_8k_v3/zero_ru.cd_cont_4000'
PATH_JSGF   = '/home/robot/Загрузки/zero_ru_cont_8k_v3/grammar.jsgf'
PATH_DIC    = '/home/robot/Загрузки/zero_ru_cont_8k_v3/transcr.dic'

path_file = (Path(__file__).parent.parent.parent.parent.absolute() / 'sound.json')
with open(path_file, 'w') as j_file:
    j_file.write(json.dumps({'sound':''}))
    
rospy.init_node('sound_processing')
os.environ['SOUND'] = ''
sound_publisher = rospy.Publisher('mic_sound', String, queue_size=10)

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=1024,
    no_search=True,
    full_utt=False,
    hmm=os.path.join(model_path, PATH_HMM),
    lm=False,
    jsgf = os.path.join(model_path, PATH_JSGF),
    dic=os.path.join(model_path, PATH_DIC)
)


for query in speech:
    with open(path_file, 'w') as j_file:
        j_file.write(json.dumps({'sound':str(query)}))
    rospy.logwarn(query)

    _str = String()
    _str.data = str(query)

    sound_publisher.publish(_str)

rospy.spin()
