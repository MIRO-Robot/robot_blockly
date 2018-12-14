#!/usr/bin/env python3
# Author: Matt Whelan

from flask import Flask, render_template, Response
import rospy
from sensor_msgs.msg import Range, Image, CompressedImage
from std_msgs.msg import String

import numpy as np
import cv2
import sys
import os

rospy.init_node('image_server', anonymous=True, disable_signals=True)
rate = rospy.Rate(100)
app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(stream_name=""):
    """Video streaming generator function."""
    try:
        while True:
            try:
                if stream_name == "right":
                    topic = '/miro/sim01/platform/camr/compressed'
                elif stream_name == "left":
                    topic = '/miro/sim01/platform/caml/compressed'
                elif stream_name == "threshold":
                    topic = "/blockly/imageVariables/threshold/compressed"
                
                image_data = rospy.wait_for_message(topic, CompressedImage, timeout=10)
                
                if image_data is not None:
                #     image_name = rospy.wait_for_message('/blocklyVariables/image_name', String, timeout=1)
                #     if image_name is not None:
                #         print(image_name)
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + image_data.data + b'\r\n')
            except rospy.exceptions.ROSException as e:
                pass
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        rospy.signal_shutdown("interrupt")


@app.route('/miro_left')
def miro_left():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen("left"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/miro_right')
def miro_right():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen("right"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/colour_thresh')
def colour_thresh():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen("threshold"),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
