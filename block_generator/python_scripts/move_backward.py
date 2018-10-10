
#-----------------------------START MOVE_BACKWARD---------------------------------
body_vel = Twist()
body_vel.angular.x = 0
body_vel.linear.x = -500
q.body_vel = body_vel

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
    rate.sleep()

pub.publish(q)
body_vel.linear.x = 0
q.body_vel = body_vel
time.sleep(1.5)
pub.publish(q)
#-----------------------------END MOVE_BACKWARD---------------------------------
