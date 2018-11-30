# -*- coding: utf-8 -*-
"""
A function to rank parameter based on precision (ability to not label a negative)

@author: Jeff Xie
"""
import matplotlib.pyplot as plt
import numpy as np
import time
from knndtw import KnnDtw
from knndtw import ProgressBar
from scipy import stats

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import precision_recall_fscore_support as score

def param_ranking(param_list,k_val,warp_val,datapath,avg_type):
    start_time = time.time()
    p = []
    r = []
    f = []
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
    
       
        # Convert to numpy for efficiency
       
        
        x_train = np.array(x_train)
        y_train = np.array(y_train)
        x_test = np.array(x_test)
        y_test = np.array(y_test)
        
        m = KnnDtw(n_neighbors=k_val, max_warping_window=warp_val)
        m.fit(x_train, y_train)
        label, proba = m.predict(x_test)
        
        precision, recall, f_score, _ = score(y_test,label,average=avg_type)
        p.append(precision)
        r.append(recall)
        f.append(f_score)
  
    precision_rank = sorted(list(zip(param_list,p)),key=lambda x: x[1])
    recall_rank = sorted(list(zip(param_list,r)),key=lambda x: x[1])
    fscore_rank = sorted(list(zip(param_list,f)),key=lambda x: x[1])
    #("Parameter rank by precision is:",precision_rank)
    print('Ranking for k = %s, max warping window = %s' %(k_val,warp_val))
    for rank in precision_rank[::-1]:
        print(rank[0],": ",rank[1])
    #print("Parameter rank by recall is:",recall_rank)
    #print("Parameter rank by f-score is:",fscore_rank)
    print("--- %s seconds ---" % (time.time() - start_time)) #let's see how long this takes...
#Testing
plist1 = ['mavlink_raw_imu_t_Xaccel','mavlink_raw_imu_t_Yaccel','mavlink_raw_imu_t_Zaccel','mavlink_raw_imu_t_XGyro','mavlink_raw_imu_t_YGyro','mavlink_raw_imu_t_ZGyro']
plist2 = ['mavlink_attitude_t_pitch angle','mavlink_attitude_t_roll angle','mavlink_attitude_t_yaw angle','mavlink_attitude_t_pitch rate','mavlink_attitude_t_yaw rate','mavlink_attitude_t_roll rate']
plist3 = ['mavlink_raw_imu_t_XMag','mavlink_raw_imu_t_YMag','mavlink_raw_imu_t_ZMag','mavlink_vibration_t_vibration_x','mavlink_vibration_t_vibration_y','mavlink_vibration_t_vibration_z']
p_all = plist1+plist2+plist3
param_ranking(p_all,1,100,'Data6/','weighted')
#param_ranking(p_all,1,100,'Data4/','weighted')