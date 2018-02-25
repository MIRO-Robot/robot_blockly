from miro_msgs.msg import platform_control
from geometry_msgs.msg import Twist
from time import sleep

if ('current_robot' not in locals()):
	current_robot = 'sim01'

pub = rospy.Publisher('/miro/' + current_robot + '/platform/control',
    platform_control, queue_size=10)
rate = rospy.Rate(10)
q = platform_control()
body_vel = Twist()
body_vel.angular.z = -0.785398	
q.body_vel = body_vel

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
	rate.sleep()
pub.publish(q)
sleep(4)	#Allow time for the turn to be executed


