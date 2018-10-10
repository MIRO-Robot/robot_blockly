
#-----------------------------START CAPTURE_IMAGE---------------------------------
timestr = time.strftime("%d-%m-%Y_%H-%M-%S.png")

# Ros Messages	 
from sensor_msgs.msg import CompressedImage

msg_image = rospy.wait_for_message('/miro/'  + current_robot + '/platform/camr/compressed', CompressedImage, timeout=7)
np_arr = np.frombuffer(msg_image.data, np.uint8)
image_np = cv2.imdecode(np_arr, 1)



rospack = rospkg.RosPack()
images_path = '/usr/local/src/robot/blockly_ws/install_isolated/share/robot_blockly/frontend/pages/images/'
cv2.imwrite(images_path+ 'image_' + timestr, image_np)

#cv2.imwrite('/home/erle/spider_ws/install_isolated/share/robot_blockly/frontend/pages/images/image_' + timestr, image_np)
#images_path = "/home/erle/spider_ws/install_isolated/share/robot_blockly/frontend/pages/images/"

files = len(os.listdir(images_path)) #amount of files in /frontend/images/ folder

if files > 7 : #allow 5 images max
    os.system("find "+images_path+" -name '*.png' | xargs ls -t | tail -n 1 | xargs rm")#remove oldest image
#-----------------------------END CAPTURE_IMAGE---------------------------------
