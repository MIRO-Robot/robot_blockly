import rospy
from sensor_msgs.msg import Range


if ('current_robot' not in locals()):
	current_robot = 'sim01'

msg_distance = rospy.wait_for_message('/miro/' + current_robot + '/sensors/sonar_range', Range, timeout=1)
