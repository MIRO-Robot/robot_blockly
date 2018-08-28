
#-----------------------------START LIFT_NECK---------------------------------
if dropdown_lift == 'L_UP':
    direction = miro.MIRO_LIFT_MIN_RAD
elif dropdown_lift == 'L_DOWN':
    direction = miro.MIRO_LIFT_MAX_RAD
else:
    direction = (miro.MIRO_LIFT_MIN_RAD + miro.MIRO_LIFT_MAX_RAD )/2
q.body_vel = Twist()
q.body_config[1] = direction
q.body_config_speed[1] = miro.MIRO_P2U_W_LEAN_SPEED_INF

#ensures that at least one node is connected before sending message
while(pub.get_num_connections() == 0):
    rate.sleep()
pub.publish(q)
sleep(3)#Allow time for the move to be executed
#-----------------------------END LIFT_NECK---------------------------------
