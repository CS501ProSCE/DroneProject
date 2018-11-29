
# -*- coding: utf-8 -*-
"""
A function to see the best k for each parameter

@author: Jeff Xie
"""
import matplotlib.pyplot as plt
import numpy as np
import time
from knndtw import KnnDtw
from knndtw import ProgressBar
from scipy import stats

from k_fold_cv import k_fold_cross_val
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import precision_recall_fscore_support as score

def find_best_k(param_list,k_range,warp_val,datapath,folds): 
    start_time = time.time()
    param_k = []
    for dataparam in param_list:
        trainingdatafile =  datapath + 'train_' + dataparam + '.txt'
        traininglabelfile = datapath + 'train_labels.txt'
         
        testdatafile =  datapath + 'test_' + dataparam + '.txt'
        testlabelfile = datapath + 'test_labels.txt'
        
        # Open training data file, x:data, y:label
        x_train_file = open(trainingdatafile, 'r')
        y_train_file = open(traininglabelfile, 'r')
        
        #Open test data file, x:data, y:label
        x_test_file = open(testdatafile, 'r')
        y_test_file = open(testlabelfile, 'r')
        
        
        # Create empty lists
        x_train = []
        y_train = []
        x_test = []
        y_test = []
        
        # Mapping table for classes
        labels = {1:'Hover', 2:'Impact (Front Left)', 3:'Impact (Front Right)', 4:'Impact (Back Left)', 5:'Impact (Back Right)', 
          6:'Gust (from Left)', 7:'Gust (from Right)', 8: 'Gust (from front)' }
        
        i = 0
        # Loop through datasets
        for x in x_train_file:
            x_train.append([float(ts) for ts in x.split()])
        for y in y_train_file:
            y_train.append(int(y.rstrip('\n')))
        
        for x in x_test_file:
            x_test.append([float(ts) for ts in x.split()])
        
        for y in y_test_file:
            y_test.append(int(y.rstrip('\n')))
        
        
        
        #close data files
        x_train_file.close()
        y_train_file.close()
        x_test_file.close()
        y_test_file.close()   
           
        # Convert to numpy for efficienc 
        x_train = np.array(x_train)
        y_train = np.array(y_train)
        x_test = np.array(x_test)
        y_test = np.array(y_test)
        
        k_best = k_fold_cross_val(k_range,x_train,y_train,folds)    
        param_k.append((dataparam,k_best))


    print("k-fold cross val results for the included paramters")    
    for kv in param_k:
         print(kv[0],": ",kv[1])
    print("--- %s seconds ---" % (time.time() - start_time)) #let's see how long this takes...
#Testing 
plist1 = ['mavlink_raw_imu_t_Xaccel','mavlink_raw_imu_t_Yaccel','mavlink_raw_imu_t_Zaccel','mavlink_raw_imu_t_XGyro','mavlink_raw_imu_t_YGyro','mavlink_raw_imu_t_ZGyro']
plist2 = ['mavlink_attitude_t_pitch angle','mavlink_attitude_t_roll angle','mavlink_attitude_t_yaw angle','mavlink_attitude_t_pitch rate','mavlink_attitude_t_yaw rate','mavlink_attitude_t_roll rate']
plist3 = ['mavlink_raw_imu_t_XMag','mavlink_raw_imu_t_YMag','mavlink_raw_imu_t_ZMag','mavlink_vibration_t_vibration_x','mavlink_vibration_t_vibration_y','mavlink_vibration_t_vibration_z']
p_all = plist1+plist2+plist3
k_list = list(range(1,6))
find_best_k(p_all,k_list,100,'Data4/',5)       