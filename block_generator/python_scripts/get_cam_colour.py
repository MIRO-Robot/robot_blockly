
#-----------------------------START GET_CAM_COLOUR---------------------------------
colorBGR = "0,100,0"
#colorBGR (colour picker input)
inB = int(colorBGR.split(',')[0])
inG = int(colorBGR.split(',')[1])
inR = int(colorBGR.split(',')[2])

image_msg = rospy.wait_for_message('/miro/' + current_robot + '/platform/caml', Image, timeout=10)

h  = image_msg.height
w  = image_msg.width
data = np.frombuffer(image_msg.data, np.uint8)

# Find central(-ish) pixel, bottom right one in a even x even image
position = (h/2) * w + w/2

# get the 3 colour components of the central pixel
B = data[position]
G = data[position + 1]
R = data[position + 2]

th = 15
result = False
if abs(inB - B) <= th and abs(inG - G) <= th and abs(inR - R) <= th:
    result = True
#-----------------------------END GET_CAM_COLOUR---------------------------------
