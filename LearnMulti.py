"""
CS501 Group 16
Fall 2018
Written by Thomas SHaw

This module calls the multi_param_learn function with multiple inputs

"""

from multi_param_learn import multi_param_learn

paramlist = ['mavlink_raw_imu_t_XGyro','mavlink_raw_imu_t_YGyro','mavlink_ahrs3_t_roll','mavlink_raw_imu_t_Zaccel','mavlink_raw_imu_t_XMag','mavlink_raw_imu_t_YMag','mavlink_vibration_t_vibration_z']
paramweight = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0]
datapath = 'Data2/'

multi_param_learn(paramlist,paramweight,datapath)