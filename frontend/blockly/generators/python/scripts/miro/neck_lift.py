LIFTfrom miro_msgs.msg import platform_control
from time import sleep


if ('current_robot' not in locals()):
	current_robot = 'sim01'

pub = rospy.Publisher('/miro/' + current_robot + '/platform/control',
    platform_control, queue_size=10)

rate = rospy.Rate(10)
q = platform_control()

if dropdown_lift == 'Y_UP':
    direction = miro.MIRO_LIFT_MAX_RAD
elif dropdown_lift == 'Y_DOWN':
    direction = miro.MIRO_LIFT_MIN_RAD
else:
    direction = (miro.MIRO_LIFT_MIN_RAD + miro.MIRO_LIFT_MAX_RAD )/2

q.body_config[1] = direction
q.body_config_speed[1] = miro.MIRO_P2U_W_LEAN_SPEED_INF

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
	rate.sleep()
pub.publish(q)
sleep(4)	#Allow time for the move to be executed
