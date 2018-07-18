import rospy
from sensor_msgs.msg import Image  # ,CompressedImage

#colorBGR (colour picker input)
inB = int(colorBGR.split(',')[0])
inG = int(colorBGR.split(',')[1])
inR = int(colorBGR.split(',')[2])

if ('current_robot' not in locals()):
	current_robot = 'sim01'

# msg_distance = rospy.wait_for_message('/miro/' + current_robot + '/sensors/sonar_range', Range, timeout=1)

image_msg = rospy.wait_for_message('/miro/' + current_robot + '/platform/' + cam_location, Image, timeout=10)
else
h  = image_msg.height
w  = image_msg.width
data = image_msg.data

# Find central(-ish) pixel, bottom right one in a even x even image
position = ((h/2) * w + w/2) * 3

# get the 3 colour components of the central pixel
B = data[position]
G = data[position + 1]
R = data[position + 2]

th = 15
result = False
if math.abs(inB - B) <= th and math.abs(inG - G) <= th and math.abs(inR - R) <= th:
	result = True
