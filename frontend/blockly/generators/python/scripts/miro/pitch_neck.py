
#-----------------------------START PITCH_NECK---------------------------------

if dropdown_pitch == 'P_UP':
    direction = miro.MIRO_PITCH_MIN_RAD
elif dropdown_pitch == 'P_DOWN':
    direction = miro.MIRO_PITCH_MAX_RAD
else:
    direction = (miro.MIRO_PITCH_MIN_RAD + miro.MIRO_PITCH_MAX_RAD )/2

q.body_vel = Twist()
q.body_config[3] = direction
q.body_config_speed[3] = miro.MIRO_P2U_W_LEAN_SPEED_INF

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
    rate.sleep()
pub.publish(q)
time.sleep(1.5)#Allow time for the move to be executed
#-----------------------------END PITCH_NECK---------------------------------
