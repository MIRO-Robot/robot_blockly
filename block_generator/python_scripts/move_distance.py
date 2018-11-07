
#-----------------------------START MOVE_DISTANCE---------------------------------

velocity = abs(velocity)
if direction != "forward":
    velocity = -velocity
    
if duration > 0:
    cycles=duration/rate.sleep_dur.to_sec()
    
    body_vel = Twist()
    body_vel.angular.x = 0
    body_vel.linear.x = velocity
    q.body_vel = body_vel

    #ensures that at least one node is connected before sending message
    while(pub.get_num_connections() == 0):
        rate.sleep()
    
    for i in range(int(cycles)):
        pub.publish(q)
        rate.sleep()
    
    body_vel.linear.x = 0
    q.body_vel = body_vel
    pub.publish(q)	#Allow time for the move to be executed
#-----------------------------END MOVE_DISTANCE---------------------------------
