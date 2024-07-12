
import os
from pocketsphinx import LiveSpeech, get_model_path
import wave, librosa, pyaudio

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=1024,
    no_search=True,
    full_utt=False,
    hmm=os.path.join(model_path, '/home/robot/Загрузки/zero_ru_cont_8k_v3/zero_ru.cd_cont_4000'),
    lm=False,
    jsgf = os.path.join(model_path, '/home/robot/Загрузки/zero_ru_cont_8k_v3/grammar.jsgf'),
    dic=os.path.join(model_path, '/home/robot/Загрузки/zero_ru_cont_8k_v3/transcr.dic')
)

print("Say something!")

for phrase in speech:

    _split_phrase = str(phrase).split(' ')
    if _split_phrase[0] == 'ERROR:':
        pass
    elif _split_phrase[0] == 'WARN:':
        pass
    else:
        pass