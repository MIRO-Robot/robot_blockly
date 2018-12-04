
#-----------------------------START SETUP_MIRO---------------------------------
from miro_msgs.msg import platform_control
from miro_constants import miro
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range, Image, CompressedImage
from std_msgs.msg import Float32MultiArray
import sys
import rospy
import subprocess
import rosnode
import numpy as np
import cv2
import time
import os
import math
import rospkg

if miro_type == "physical":
    current_robot = 'rob01'
else:
    current_robot = 'sim01'

pub = rospy.Publisher('/miro/' + current_robot + '/platform/control', platform_control, queue_size=10)
image_pub = rospy.Publisher('/blockly/imageVariables/threshold/compressed', CompressedImage, queue_size=1, latch=True, tcp_nodelay=True)

rate = rospy.Rate(10)
q = platform_control()
#-----------------------------END SETUP_MIRO---------------------------------
