
#-----------------------------START YAW_NECK---------------------------------
if dropdown_yaw == 'Y_RIGHT':
    direction = miro.MIRO_YAW_MAX_RAD
elif dropdown_yaw == 'Y_LEFT':
    direction = miro.MIRO_YAW_MIN_RAD
else:
    direction = (miro.MIRO_YAW_MIN_RAD + miro.MIRO_YAW_MAX_RAD )/2

q.body_vel = Twist()
q.body_config[2] = direction
q.body_config_speed[2] = miro.MIRO_P2U_W_LEAN_SPEED_INF

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
    rate.sleep()
pub.publish(q)
sleep(3)	#Allow time for the move to be executed
#-----------------------------END YAW_NECK---------------------------------
