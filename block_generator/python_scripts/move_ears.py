
#-----------------------------START MOVE_EARS---------------------------------


if ears_direction == 'Forward':
    direction_value = 0
else:
     direction_value = 1
    
if ears_group == "Left":
    q.ear_rotate = [direction_value, 0]
elif ears_group == 'Right':
    q.ear_rotate = [0, direction_value]
else:
     q.ear_rotate = [direction_value, direction_value]

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
    rate.sleep()
pub.publish(q)
q.ear_rotate
#-----------------------------END MOVE_EARS---------------------------------
