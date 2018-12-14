#!/usr/bin/env python3
# Author: Daniel Camilleri

import rospy
from sensor_msgs.msg import Range, Image, CompressedImage
from std_msgs.msg import String

import numpy as np
import cv2
import sys
import os

import asyncio
import pathlib
import ssl
import websockets
import json
import base64
import time

rospy.init_node('image_server', anonymous=True, disable_signals=True)
rate = rospy.Rate(100)

async def get_ros_image(image_topic):
    try:
        if "compressed" in image_topic:
            return rospy.wait_for_message(image_topic, CompressedImage, timeout=0.5).data
        else:
            uncompressed_msg = rospy.wait_for_message(image_topic, Image, timeout=0.5)
            uncomp_arr = np.frombuffer(uncompressed_msg.data, dtype=np.uint8)
            uncompressed = np.reshape(uncomp_arr, (uncompressed_msg.height, uncompressed_msg.width, 3))
            uncompressed = cv2.cvtColor(uncompressed, cv2.COLOR_BGR2RGB)
            return cv2.imencode('.jpg', uncompressed)[1]
    except rospy.exceptions.ROSException as e:
        return None
    except Exception as e:
        print(e)
        return None


async def message_sender(websocket, path):
    print("Starting server")
    topics_list = ['/miro/sim01/platform/camr',
                   '/blockly/imageVariables/threshold/compressed']

    topic_names = ["Right Camera", "Colour Threshold"]

    counters = [0] * len(topics_list)
    inc = 0
    freq = 10

    start_t = time.time()
    try:
        while True:
            msg_dict = dict()
            tasks = [get_ros_image(topic_name) for topic_name in topics_list]

            # schedule the tasks and retrieve results
            results = await asyncio.gather(*tasks)
            # print(results)

            for i, r in enumerate(results):
                if r is not None:
                    counters[i] += 1

                    msg_dict["image_" + str(i)] = \
                    {"name": topics_list[i],
                     "variable_name": topic_names[i],
                     "data": base64.b64encode(r).decode("utf-8")}

            if len(msg_dict) > 0:
                json_obj = json.dumps(msg_dict)
                await websocket.send(json_obj)

    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        rospy.signal_shutdown("interrupt")


# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# ssl_context.load_cert_chain(
#     pathlib.Path(__file__).with_name('localhost.pem'))

# start_server = websockets.serve(message_sender, 'localhost', 5000, ssl=ssl_context)
start_server = websockets.serve(message_sender, "0.0.0.0", 5000)

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
# loop.run_until_complete(message_sender)

try:
    loop.run_forever()
except KeyboardInterrupt as e:
    pass
finally:
    loop.close()
