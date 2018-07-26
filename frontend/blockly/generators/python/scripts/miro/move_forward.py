#-----------------------------START MOVE FORWARD---------------------------------

body_vel = Twist()
body_vel.angular.x = 0
body_vel.linear.x = +200
q.body_vel = body_vel

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
	rate.sleep()
pub.publish(q)
sleep(3)	#Allow time for the move to be executed

#-----------------------------END MOVE FORWARD---------------------------------
