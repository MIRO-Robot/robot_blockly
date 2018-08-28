
#-----------------------------START SETUP_MIRO---------------------------------
from miro_constants import miro
from miro_msgs.msg import platform_control
from geometry_msgs.msg import Twist
from time import sleep

if ('current_robot' not in locals()):
    current_robot = 'sim01'

pub = rospy.Publisher('/miro/' + current_robot + '/platform/control',
    platform_control, queue_size=10)
rate = rospy.Rate(10)
q = platform_control()
#-----------------------------END SETUP_MIRO---------------------------------
