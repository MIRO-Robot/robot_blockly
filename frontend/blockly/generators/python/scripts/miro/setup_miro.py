from miro_msgs.msg import platform_control
from geometry_msgs.msg import Twist
from miro_constants import miro
from time import sleep
import rospy
from sensor_msgs.msg import Range, Image  # ,CompressedImage

if ('current_robot' not in locals()):
	current_robot = 'sim01'

pub = rospy.Publisher('/miro/' + current_robot + '/platform/control',
    platform_control, queue_size=10)
rate = rospy.Rate(10)
q = platform_control()
