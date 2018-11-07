
#-----------------------------START TURN_ANGLE---------------------------------


angular_velocity = abs(angular_velocity)
if direction != "anticlockwise":
    angular_velocity = -angular_velocity

if duration > 0:
    cycles=duration/rate.sleep_dur.to_sec()
    body_vel = Twist()
    body_vel.angular.z = angular_velocity
    q.body_vel = body_vel

    #ensures that at least one node is connected before sending message
    while(pub.get_num_connections() == 0):
        rate.sleep()
    
    for i in range(int(cycles)):
        pub.publish(q)
        rate.sleep()
    
    body_vel.angular.z = 0
    pub.publish(q)
#-----------------------------END TURN_ANGLE---------------------------------
