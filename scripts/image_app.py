#!/usr/bin/env python3
# Author: Matt Whelan

from flask import Flask, render_template, Response
import rospy
from sensor_msgs.msg import Range, Image, CompressedImage

import numpy as np
import cv2
import sys
import os

rospy.init_node('image_server', anonymous=True, disable_signals=True)
rate = rospy.Rate(10)
app = Flask(__name__)
current_robot = "sim01"

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
    try:
        while True:
            image_l = rospy.wait_for_message('/miro/' + current_robot + '/platform/caml/compressed', CompressedImage, timeout=10)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + image_l.data + b'\r\n')
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        rospy.signal_shutdown("interrupt")


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)