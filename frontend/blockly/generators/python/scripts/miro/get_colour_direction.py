
#-----------------------------START GET_COLOUR_DIRECTION---------------------------------
hex_str = hex_string.lstrip("#")
lv = len(hex_str)
colorRGB = tuple(int(hex_str[i:i+ lv // 3], 16) for i in range(0, lv, lv // 3))
colorHSV = np.full([1,1,3], colorRGB, dtype=np.uint8)
colorHSV = cv2.cvtColor(colorHSV, cv2.COLOR_RGB2HSV)[0,0]

image_l = rospy.wait_for_message('/miro/' + current_robot + '/platform/caml', Image, timeout=10)
image_r = rospy.wait_for_message('/miro/' + current_robot + '/platform/camr', Image, timeout=10)
h  = image_l.height
w  = image_l.width
data_l = np.frombuffer(image_l.data, np.uint8)
data_l = np.reshape(data_l, (h, w, 3))

data_r = np.frombuffer(image_r.data, np.uint8)
data_r = np.reshape(data_r, (h, w, 3))

frac = int(round(w/2))
data = np.hstack([data_l[:,-frac:,:], 
                  data_r[:,:frac,:]])

hsv_image = cv2.cvtColor(data, cv2.COLOR_RGB2HSV)

offset = 30
lower = np.array([colorHSV[0]-offset, 0, 0])
upper = np.array([colorHSV[0]+offset, 255, 255])

mask = cv2.inRange(hsv_image, lower, upper)

while(image_pub.get_num_connections() == 0):
    rate.sleep()

msg = CompressedImage()
msg.header.stamp = rospy.Time.now()
msg.format = "jpeg"
msg.data = np.array(cv2.imencode('.jpg', mask)[1]).tostring()
# Publish new image
image_pub.publish(msg)
time.sleep(1)

result_left = float(cv2.countNonZero(mask[:,:frac])) / mask.size
result_right = float(cv2.countNonZero(mask[:,-frac:])) / mask.size

result = result_left + result_right
if abs(result_left - result_right) < 0.05:
    result = 0 
else:
    if result_left > result_right:
        result = -1
    else:
        result = +1


#-----------------------------END GET_COLOUR_DIRECTION---------------------------------
