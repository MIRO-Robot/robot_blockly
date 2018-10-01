
#-----------------------------START MOVE_EARS---------------------------------

if dropdown_ears == 'Droop':
    q.ear_rotate = [0, 0]
elif dropdown_ears == 'Neutral':
    q.ear_rotate = [-1, -1]
else:
    q.tail = 1

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
    rate.sleep()
pub.publish(q)
time.sleep(1.5)#Allow time for the move to be executed
#-----------------------------END MOVE_EARS---------------------------------
