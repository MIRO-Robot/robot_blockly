
#-----------------------------START TURN_LEFT---------------------------------
body_vel = Twist()
body_vel.angular.z = +0.785398
q.body_vel = body_vel

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
    rate.sleep()
pub.publish(q)
time.sleep(2)
body_vel.angular.z = 0#Allow time for the move to be executed
#-----------------------------END TURN_LEFT---------------------------------
