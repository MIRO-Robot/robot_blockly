#-----------------------------START TURN RIGHT---------------------------------

body_vel = Twist()
body_vel.angular.z = -0.785398	
q.body_vel = body_vel

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
	rate.sleep()
pub.publish(q)
sleep(4)	#Allow time for the turn to be executed

#-----------------------------END TURN RIGHT---------------------------------
