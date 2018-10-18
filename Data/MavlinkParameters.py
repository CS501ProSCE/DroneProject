
mavlink_param = []
mavlink_index = []
mavlink_types = []
mavlink_rate = []

#mavlink_ahrs_t
mavlink_types.append("mavlink_ahrs_t")
rate = 35.0
param = ["timestamp","omegaIx","omegaIy","omegaIz","accel_weight","renorm_val","error_rp","error_yaw"]
index =  [1,12,14,16,18,20,22,24]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_ahrs2_t
mavlink_types.append("mavlink_ahrs2_t")
rate = 8
param = ["timestamp","roll","pitch","yaw","altitude","lat","lng"]
index =  [1,12,14,16,18,20,22]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_ahrs3_t
mavlink_types.append("mavlink_ahrs3_t")
rate = 8
param = ["timestamp","roll","pitch","yaw","altitude","lat","lng"]
index =  [1,12,14,16,18,20,22]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_attitude_t
mavlink_types.append("mavlink_attitude_t")
rate = 8.5
param = ["timestamp","time boot ms","roll angle","pitch angle","yaw angle","roll rate","pitch rate","yaw rate"]
index =  [1,12,14,16,18,20,22,24]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#TS - battery data does not change
#mavlink_battery_status_t
mavlink_types.append("mavlink_battery_status_t")
rate = 5
param = ["timestamp", "Current Consumed","Energy Consumed","Battery temperature","battery current","battery function","battery remaining","battery time remaining"]
index = [1,12,14,16,20,24,28,30]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_ekf_status_report_t
mavlink_types.append("mavlink_ekf_status_report_t")
rate = 35.0
param = ["timestamp","velocity_variance","pos_horiz_variance","pos_vert_variance","compass_variance","terrain_alt_variance","flags","airspeed_variance"]
index = [1,12,14,16,18,20,22,24]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_global_position_int_t
mavlink_types.append("mavlink_global_position_int_t")
rate = 9.0
param = ["timestamp", "time_boot_ms","lat","lon","alt","relative_alt","vx","vy","vz","hdg"]
index = [1,12,14,16,18,20,22,24,26,28]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_gps_raw_int_t
mavlink_types.append("mavlink_gps_raw_int_t")
rate = 5.0
param = ["timestamp", "time_usec","lat","lon","alt","eph","epv","vel","cog","fix_type","satelliets_visibile","alt_ellipsoid","h_acc","v_acc","vel_acc","hdg_acc"]
index = [1,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_gps2_raw_t
mavlink_types.append("mavlink_gps2_raw_t")
rate = 5.0
param = ["timestamp", "time_usec","lat","lon","alt","dgps_age","eph","epv","vel","cog","fix_type","satelliets_visibile","dgps_numch"]
index = [1,12,14,16,18,20,22,24,26,28,30,32,34]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_mission_current_t
mavlink_types.append("mavlink_mission_current_t")
rate = 10.0
param = ["timestamp", "seq"]
index = [1,12]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_nav_controller_output_t
mavlink_types.append("mavlink_nav_controller_output_t")
rate = 10.0
param = ["timestamp", "nav_roll","nav_pitch","alt_error","aspd_error","xtrack_error","nav_bearing","target_bearing","wp_dist"]
index = [1,12,14,16,18,20,22,24,26]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_raw_imu_t
mavlink_types.append("mavlink_raw_imu_t")
rate = 50.0
param = ["IMU timestamp","Xaccel","Yaccel","Zaccel","XGyro","YGyro","ZGyro","XMag","YMag","ZMag"]
index = [1,14,16,18,20,22,24,26,28,30]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_servo_output_raw_t
mavlink_types.append("mavlink_servo_output_raw_t")
rate = 8.2
param = ["Servo timestamp","Servo utime","Servo 1","Servo 2","Servo 3","Servo 4"]
index = [1,12,14,16,18,20]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_system_time_t
mavlink_types.append("mavlink_system_time_t")
rate = 35.0
param = ["timestamp","time_unix_usec","time_boot_ms"]
index = [1,12,14]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#mavlink_vibration_t
mavlink_types.append("mavlink_vibration_t")
rate = 35.0
param = ["timestamp","vibration_x","vibration_y","vibration_z"]
index = [1,14,16,18]
mavlink_param.append(param)
mavlink_index.append(index)
mavlink_rate.append(rate)

#error check parameters to avoid nasty surprises
for typ in range(len(mavlink_types)):
    if(len(mavlink_param[typ]) != len(mavlink_index[typ])):
        raise ValueError("ERROR: mavlink type " + mavlink_types[typ] + " has mismatched index and param size")
