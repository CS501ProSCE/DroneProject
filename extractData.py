"""
CS 50100 Group 16
Python script to extract raw drone data from Mission Planner output

1. input csv file name
2. determine if you want to cut sample 
3. xlsx file will be output as "Data_filenmame.xlsx"

"""

import openpyxl as op
import numpy as np
import datetime


#change this to name of file - MUST BE in XLS format to work with openpyxl!!
name = "2018-10-07 13-59-17.csv"

#Define data time parameters
cuttime = False  #define True if you want to cut to start and stop times
starttime = "2018-10-07T13:59:54.433"  #Data will start at this time,define as None if no crop desired
endtime = "2018-10-07T14:01:51.048" #Data will end at this time, define as Non if no end crop desired

if(cuttime):
    starttime = starttime.replace("T"," ")
    endtime = endtime.replace("T"," ")
    startt = datetime.datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S.%f')
    endt = datetime.datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S.%f')
    print("This will process file %s"%(name))
    print("The data will start at %s"%(startt))
    print("The data will end at %s"%(endt))


mavlink_param = []
mavlink_index = []
mavlink_types = []

#mavlink_ahrs_t
mavlink_types.append("mavlink_ahrs_t")
param = ["timestamp","omegaIx (rad/s)","omegaIy (rad/s)","omegaIz (rad/s)","accel_weight","renorm_val","error_rp","error_yaw"]
index =  [1,12,14,16,18,20,22,24]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_ahrs2_t
mavlink_types.append("mavlink_ahrs2_t")
param = ["timestamp","roll","pitch","yaw","altitude","lat","lng"]
index =  [1,12,14,16,18,20,22]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_ahrs3_t
mavlink_types.append("mavlink_ahrs3_t")
param = ["timestamp","roll","pitch","yaw","altitude","lat","lng"]
index =  [1,12,14,16,18,20,22]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_attitude_t
mavlink_types.append("mavlink_attitude_t")
param = ["timestamp","time boot ms","roll angle","pitch angle","yaw angle","roll rate","pitch rate","yaw rate"]
index =  [1,12,14,16,18,20,22,24]
mavlink_param.append(param)
mavlink_index.append(index)

#TS - battery data does not change
#mavlink_battery_status_t
#mavlink_types.append("mavlink_battery_status_t")
#param = ["timestamp", "Current Consumed","Energy Consumed","Battery temperature","battery current","battery function","battery remaining","battery time remaining"]
#index = [1,12,14,16,20,24,28,30]
#mavlink_param.append(param)
#mavlink_index.append(index)

#mavlink_ekf_status_report_t
mavlink_types.append("mavlink_ekf_status_report_t")
param = ["timestamp","velocity_variance","pos_horiz_variance","pos_vert_variance","compass_variance","terrain_alt_variance","flags","airspeed_variance"]
index = [1,12,14,16,18,20,22,24]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_global_position_int_t
mavlink_types.append("mavlink_global_position_int_t")
param = ["timestamp", "time_boot_ms","lat","lon","alt","relative_alt","vx","vy","vz","hdg"]
index = [1,12,14,16,18,20,22,24,26,28]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_gps_raw_int_t
mavlink_types.append("mavlink_gps_raw_int_t")
param = ["timestamp", "time_usec","lat","lon","alt","eph","epv","vel","cog","fix_type","satelliets_visibile","alt_ellipsoid","h_acc","v_acc","vel_acc","hdg_acc"]
index = [1,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_gps2_raw_t
mavlink_types.append("mavlink_gps2_raw_t")
param = ["timestamp", "time_usec","lat","lon","alt","dgps_age","eph","epv","vel","cog","fix_type","satelliets_visibile","dgps_numch"]
index = [1,12,14,16,18,20,22,24,26,28,30,32,34]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_mission_current_t
mavlink_types.append("mavlink_mission_current_t")
param = ["timestamp", "seq"]
index = [1,12]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_nav_controller_output_t
mavlink_types.append("mavlink_nav_controller_output_t")
param = ["timestamp", "nav_roll","nav_pitch","alt_error","aspd_error","xtrack_error","nav_bearing","target_bearing","wp_dist"]
index = [1,12,14,16,18,20,22,24,26]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_raw_imu_t
mavlink_types.append("mavlink_raw_imu_t")
param = ["IMU timestamp","Xaccel","Yaccel","Zaccel","XGyro","YGyro","ZGyro","XMag","YMag","ZMag"]
index = [1,14,16,18,20,22,24,26,28,30]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_servo_output_raw_t
mavlink_types.append("mavlink_servo_output_raw_t")
param = ["Servo timestamp","Servo utime","Servo 1","Servo 2","Servo 3","Servo 4"]
index = [1,12,14,16,18,20]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_system_time_t
mavlink_types.append("mavlink_system_time_t")
param = ["timestamp","time_unix_usec","time_boot_ms"]
index = [1,12,14]
mavlink_param.append(param)
mavlink_index.append(index)

#mavlink_vibration_t
mavlink_types.append("mavlink_vibration_t")
param = ["timestamp","vibration_x","vibration_y","vibration_z"]
index = [1,14,16,18]
mavlink_param.append(param)
mavlink_index.append(index)


#error check
for typ in range(len(mavlink_types)):
    if(len(mavlink_param[typ]) != len(mavlink_index[typ])):
        print("ERROR: mavlink type %s has mismatched index and param size" %(mavlink_types[typ]))

#Read data from file
        
#Create list stucture
mavlink_data = []
for typ in range(len(mavlink_types)):
    typdata = []
    for _ in range(len(mavlink_param[typ])):
        typdata.append([]) 
    mavlink_data.append(typdata)

#read raw data file
filelist = []
with open(name) as f: 
    for line in f:
        filelist.append(line.split(','))
f.close()

#read data into parameter lists
for row in filelist:
    for typ in range(len(mavlink_types)):
        if(str(row[9]) == mavlink_types[typ]):
            if(cuttime):
                timestamp = row[0]
                timestamp = timestamp.replace("T"," ")
                rowtime = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
                if((rowtime>startt)and(rowtime<endt)):
                    for param in range(len(mavlink_param[typ])):
                        if(param==0):   #leave timestapm as string
                            mavlink_data[typ][param].append(row[mavlink_index[typ][param]-1])
                        else:           #convert all other to float
                            mavlink_data[typ][param].append(float(row[mavlink_index[typ][param]-1]))
                    break                      
            else:
                for param in range(len(mavlink_param[typ])):
                    if(param==0):   #leave timestapm as string
                        mavlink_data[typ][param].append(row[mavlink_index[typ][param]-1])
                    else:           #convert all other to float
                        mavlink_data[typ][param].append(float(row[mavlink_index[typ][param]-1]))
                break                    

#Create new worksheet and output data
newbook = op.Workbook()
newbook.remove_sheet(newbook.active)

ws = []
for typ in range(len(mavlink_types)):
    ws.append(newbook.create_sheet(mavlink_types[typ]))    
    for param in range(len(mavlink_param[typ])):
        ws[typ].cell(row=1,column=param+1).value = mavlink_param[typ][param]
        for row in range(len(mavlink_data[typ][param])):
            ws[typ].cell(row=row+2,column=param+1).value = mavlink_data[typ][param][row]      

newname =  "Data_" + name.replace("csv","xlsx")    
newbook.save(newname)


