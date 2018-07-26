#-----------------------------START GET DISTANCE---------------------------------

msg_distance = rospy.wait_for_message('/miro/' + current_robot + '/sensors/sonar_range', Range, timeout=1)

#-----------------------------END GET DISTANCE---------------------------------
