#! /usr/bin/python

import rospy, os
import uvicorn
from pathlib import Path
from std_msgs.msg import String, Int16MultiArray, Int8MultiArray
from fastapi import (FastAPI, Request, WebSocket)
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.websockets import WebSocketDisconnect
from typing import List
import sqlite3
rospy.init_node('tcp_web_server')

test_pub = rospy.Publisher('web_server', String, queue_size=10)
calibration_astra = rospy.Publisher('calibration_astra', Int8MultiArray, queue_size=10)
calibration_eyes = rospy.Publisher('calibration_eyes', Int8MultiArray, queue_size=10)

calibration_eyes_data = Int8MultiArray()
calibration_eyes_data.data = [0]*6

web_log_right_eye = [0,0,0]

app = FastAPI()

templates = Jinja2Templates(directory = Path(__file__).parent.absolute() / 'temp')

app.mount(f'{Path(__file__).parent.absolute() / "ui"}', 
            StaticFiles(directory=Path(__file__).parent.absolute() / "ui", html=True), name='ui')

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


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


async def ros_topic_send():
    global calibration_eyes
    global calibration_eyes_data

    await calibration_eyes.publish(calibration_eyes_data)


def log_eye_data(data):
    global web_log_right_eye

    web_log_right_eye[0] = data.data[0]
    web_log_right_eye[1] = data.data[1]
    web_log_right_eye[2] = data.data[2]


@app.websocket("/eyes_calibrate")
async def websocket_heandler(websocket:WebSocket):
    
    manager = ConnectionManager()

    global calibration_eyes_data
    global web_log_right_eye

    await manager.connect(websocket)
    try:
        while True:
            _data = await websocket.receive_json()
            try:
                calibration_eyes_data.data[0] = int(_data['slider0'])
                calibration_eyes_data.data[1] = int(_data['slider1'])
                calibration_eyes_data.data[2] = int(_data['slider2'])
                calibration_eyes_data.data[3] = int(_data['slider3'])
                calibration_eyes_data.data[4] = int(_data['slider4'])
                calibration_eyes_data.data[5] = int(_data['slider5'])

            except KeyError:

                calibration_eyes_data.data[0] = 0
                calibration_eyes_data.data[1] = 0
                calibration_eyes_data.data[2] = 0
                calibration_eyes_data.data[3] = 0
                calibration_eyes_data.data[4] = 0
                calibration_eyes_data.data[5] = 0

            except Exception:

                calibration_eyes_data.data[0] = 0
                calibration_eyes_data.data[1] = 0
                calibration_eyes_data.data[2] = 0
                calibration_eyes_data.data[3] = 0
                calibration_eyes_data.data[4] = 0
                calibration_eyes_data.data[5] = 0
                
            if _data['message'] == 'ok':    
                await manager.send_personal_message({'message':'ok', 'right_eye_log':web_log_right_eye}, websocket=websocket)
            else:
                pass
            

    
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception:
        pass

if __name__ == '__main__':

    uvicorn.run(app = app, host='10.42.0.1', port=8282)
    rospy.Subscriber('/web_log_right_eye', Int16MultiArray, callback=log_eye_data)
    rospy.spin()