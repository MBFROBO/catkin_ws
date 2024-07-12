Описание проекта для конкурса*

#### 1. Описание работы алгоритма рукопожатия

     Для начала, следует понимать, что управление осщуествялется сверху вниз. От глазных камер с учётом голосовых команд, до конечного привода руки.

    Программное обеспечение для робота промобота построенно вокруг[ ROS.](https://www.ros.org/) Верхний уровень написан на Python, нижний уровень на Arduino C++.

######   1.1 Считываение данных с глазных камер

    Считывание данных с камер происходит через USB порт в ПК на роботе. Данные напрямую читаются [нодой]([rospy/Overview/Initialization and Shutdown - ROS Wiki](https://wiki.ros.org/rospy/Overview/Initialization%20and%20Shutdown)). Данная нода, **robot_eyes/scripts/robot_eyes.py**, а точнее, часть её скрипта, описана ниже.

```python
     success, image = cap.read()
        imageRGB = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = hands.process(imageRGB)
        rospy.logwarn(os.environ['astra_data'])
        if (int(os.environ['astra_data']) == 0 or int(os.environ['astra_data']) == 1):
            data_face.data=[0.0,0.0] # Если надо пожать руку - флаг лица 0 

        if results.multi_hand_landmarks and (int(os.environ['astra_data']) == 0 or int(os.environ['astra_data']) == 1):
            
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)

                    cx_array.append(int(cx))
                    cy_array.append(int(cy)) 
   
```

    На данном выше фрагменте кода описывается получение изображения с камер. Принятие решения по обработке камеры осуществялется с помощью флага **"astra_data"** (флаг подробно описан в 1.2). Переменная **results** содержит в себе ссылку на объект класса **mpHand** мощнейшего нейросетевого интрумента [mediapipe]([GitHub - google-ai-edge/mediapipe: Cross-platform, customizable ML solutions for live and streaming media.](https://github.com/google-ai-edge/mediapipe), используемый для определния кистей рук и лица человека в транслируемом видеопотоке.

    Так как поток видео стриминговый, то каждый кадр видео проходит через обработку нейросети.

###### 1.2 Считывание данных с астра камеры

    [Astra camera](https://husarion.com/tutorials/ros-equipment/astra/) или ORBEC в нашем случае действует в RGB и ИК-спектре. В ИК спектре происходит разброс облака точек для определения удалённости объекта от ИК-датчика камеры.

    В данном проекте эта камера изначально использвалась как дальномер, алгоритм которого представлен на вставке ниже

```python
 try:
        cv_image = bridge.imgmsg_to_cv2(data, "16UC1")
    except CvBridgeError as e:
        print('CV_BRIDGE_ERROR: ',e)

    img2 = np.float32(cv_image) * 0.0001
    standart_img.publish(bridge.cv2_to_imgmsg(img2, '32FC1'))

    cv_image_convert_uint8_t = img_as_ubyte(img2)
    cv_image_convert_uint8_t = cv.blur(cv_image_convert_uint8_t,(1,1))

    frame_threshold_1 = cv.inRange(cv_image_convert_uint8_t, 1, 15)
    frame_threshold_2 = cv.inRange(cv_image_convert_uint8_t, 20, 30)
    frame_threshold_3 = cv.inRange(cv_image_convert_uint8_t, 35, 50)

    contours_1, hierarchy_1 = cv.findContours(frame_threshold_1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_2, hierarchy_2 = cv.findContours(frame_threshold_2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours_3, hierarchy_3 = cv.findContours(frame_threshold_3, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    drawing = np.zeros((/.shape[0], cv_image_convert_uint8_t.shape[1], 3), dtype=np.uint8)
```

      Так же расписан алгоритм рисования контура на выводе. Этот момент описан подробно в 2.1.

    Дальномер описан функцией **cv.inRange** и переменными **frame_threshold_**.

    Нода Astra camera публикует **"astra_data"** к поддписчикам ноды, в том числе, в **robot_eyes.py**.

###### 1.3 Определение речи

Для определения речи в топике **sound_processing** используется библиотека [pocketsphinx]([pocketsphinx · PyPI](https://pypi.org/project/pocketsphinx/)). По умолчанию, в режиме автономной работы, библиотека не имеет поддрежки русского синтаксиса. Это оказалось необходимым, так как для понимания команд нужно перевести речь в символы. Далее отталкиваться от записанного словаря команд.

```python
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
```

    На вставке выше приведён фрагмент кода с обработкой речи через LifeSpeech. Для определения русского языка пришлось установить языковой пакет, однако, алгоритм поиска по 15 000 словам для фразы из нескольких слов работал очень медленно (что логично).

    Удалось ускорить работу алгоритма благодаря написанию собственной грамматики, сокращения доступных слов, и задать рамки, описав правила расстановки слов.

    Результатом является то, что с помощью команд стало возможным переключать режимы робота (с рукопожатия на набюджение и наоборот). Так как этот модуль добавлялся последним и изначально продуман не был, пришлось имитировать приближение к astra camera и при определённой команде задавать соответствующее положение флага **"astra_data"**.

#### 2 Вывод данных

    Для пользователя доступно несолько способов получения обратной связи от робота, описанные в 2.1 и в 2.2

###### 2.1 Вывод на планшет

    Под видом ROS-ноды был поднят веб-сервер на базе [fastapi](https://fastapi.tiangolo.com/).

```python
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('index.html', context={'request':request})

@app.get("/eyes_calibrate")
async def root(request: Request):
    return templates.TemplateResponse('calibration_eyes.html', context={'request':request})

@app.get("/astra_calibrate")
async def root(request: Request):
    return templates.TemplateResponse('calibration_astra.html', context={'request':request})
@app.get("/promo")
async def promo(request:Request):
    return templates.TemplateResponse('promo.html', context={'request':request})
```

    Выходной сигнал получается следующим. Так, на рисунке ниже изображён выход по астра кемере (1.2)
![](/home/robot/.config/marktext/images/2024-07-12-17-52-35-image.png)
![](file:///home/robot/.config/marktext/images/2024-07-12-17-52-35-image.png?msec=1720795955921)

На следующем рисунке изобржена работа нейросети по глазным камерам (1.1)

![](https://sun9-30.userapi.com/impg/ld_wxzIZlvn7K6TaZ5xR9HYnRJ_-8pln_FwnmQ/aMLyyRrK2ks.jpg?size=1035x687&quality=95&sign=31878ae366a8db602a233c7fc08c6cc8&type=album)

Общий вид промобота на следующем рисунке

![](https://sun9-10.userapi.com/impg/OkbJ078QkP1_Qsaz-SnEwNVhcwCmiXIPeBDbUg/M-6dwQ4296Q.jpg?size=1215x2160&quality=95&sign=e38028e64afac2f6f3f02c70300da5fa&type=album)

Процесс приёма передачи стриминговых данных осуществлялся через промежуточный веб-сервер **web_video_server**.
