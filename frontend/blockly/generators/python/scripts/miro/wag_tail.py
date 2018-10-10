
#-----------------------------START WAG_TAIL---------------------------------

if dropdown_wag == 'Droop':
    q.tail = -1
elif dropdown_wag == 'Neutral':
    q.tail = 0
else:
    q.tail = 1

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
    rate.sleep()
pub.publish(q)
time.sleep(1.5)
q.tail = 0#Allow time for the move to be executed
#-----------------------------END WAG_TAIL---------------------------------
