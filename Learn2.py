"""
CS501 Group 16
Fall 2018
Modified/adapted from code baseline by Thomas Shaw

This module executes the algorithm on all parameters in MavlinkParameters.py, and uses the 
individual parameter identification set to vote for an overall identification

Re-used code from: https://github.com/markdregan/K-Nearest-Neighbors-with-Dynamic-Time-Warping
credit: Mark Dregan

*Some modifications made for implementation in Python3 and custom data input, plotting

"""


import matplotlib.pyplot as plt
import numpy as np

from knndtw import KnnDtw
from knndtw import ProgressBar

from MavlinkParameters import mavlink_types
from MavlinkParameters import mavlink_param

dataset = 'Data/'
analyzelist = ['mavlink_raw_imu_t_XGyro','mavlink_raw_imu_t_YGyro','mavlink_raw_imu_t_Zaccel']

plot_data_on = False        #This will plot training and test data samples for all cases
confusion_matrix_on = True  #this will plot confusion matrix for all cases
AnalyzeAll = False           #This will ignore ANalyzeList and analyze ALL parameters

param_def = []

for typ in range(len(mavlink_types)):
    for param in range(1,len(mavlink_param[typ])):
        
        dataparam = mavlink_types[typ] + '_' + mavlink_param[typ][param]
        
        if((dataparam in analyzelist) or (AnalyzeAll)):
            
            print('Analyzing data set %s' %(dataparam))
            trainingdatafile =  dataset + 'train_' + dataparam + '.txt'
            traininglabelfile = dataset + 'train_labels.txt'
            
            testdatafile =  dataset + 'test_' + dataparam + '.txt'
            testlabelfile = dataset + 'test_labels.txt'
            
            # Import the HAR dataset
            x_train_file = open(trainingdatafile, 'r')
            y_train_file = open(traininglabelfile, 'r')
            
            x_test_file = open(testdatafile, 'r')
            y_test_file = open(testlabelfile, 'r')
            
            # Create empty lists
            x_train = []
            y_train = []
            x_test = []
            y_test = []
            
            # Mapping table for classes
            labels = {1:'Hover', 2:'Impact (tapping)', 3:'Wind'}
            
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
            
            
            #plot train data
            if(plot_data_on):
                plt.figure(figsize=(11,7))
                colors = ['#D62728','#2C9F2C','#FD7F23','#1F77B4','#9467BD',
                          '#8C564A','#7F7F7F','#1FBECF','#E377C2','#BCBD27',
                          '#D62728','#2C9F2C']
                for i, r in enumerate([0,1,2,3,5,6,7,8,9,10,11,12]):
                    plt.subplot(7,2,i+1)
                    plt.plot(x_train[r], label=labels[y_train[r]], color=colors[i], linewidth=2)
                    plt.xlabel('Samples @50Hz')
                    plt.legend(loc='upper left')
                    plt.tight_layout()
                
                #Plot Test data
                plt.figure(figsize=(11,7))
                colors = ['#D62728','#2C9F2C','#FD7F23','#1F77B4','#9467BD',
                          '#8C564A','#7F7F7F','#1FBECF','#E377C2','#BCBD27']
                for i, r in enumerate([0,1,2,3,4,5]):
                    plt.subplot(3,2,i+1)
                    plt.plot(x_test[r], label=labels[y_test[r]], color=colors[i], linewidth=2)
                    plt.xlabel('Samples @50Hz')
                    plt.legend(loc='upper left')
                    plt.tight_layout()
                
            
            #Analyze dataset
            m = KnnDtw(n_neighbors=1, max_warping_window=100)
            m.fit(x_train, y_train)
            label, proba = m.predict(x_test)
            
            #Classification report
            from sklearn.metrics import classification_report, confusion_matrix
            print(classification_report(label, y_test,
                                        target_names=[l for l in labels.values()]))
            
            
            #Confusion Matrix
            if(confusion_matrix_on):
                conf_mat = confusion_matrix(label, y_test)
                
                fig = plt.figure(figsize=(3,3))
                width = np.shape(conf_mat)[1]
                height = np.shape(conf_mat)[0]
                
                res = plt.imshow(np.array(conf_mat), cmap=plt.cm.summer, interpolation='nearest')
                for i, row in enumerate(conf_mat):
                    for j, c in enumerate(row):
                        if c>0:
                            plt.text(j-.2, i+.1, c, fontsize=16)
                            
                #cb = fig.colorbar(res)
                plt.title('Confusion Matrix for ' + dataparam)
                plt.xlabel('Data')
                plt.ylabel('ML Identification')
                _ = plt.xticks(range(3), [l for l in labels.values()], rotation=90)
                _ = plt.yticks(range(3), [l for l in labels.values()])
        
            
            param_def.append(label) 



# use individual paramer results to vote for each train sample
# This is very messy for now!!!            
            
testlist = []
for i in range(len(param_def[0])):
    testlist.append([])

for i in range(len(param_def)):
    for k in range(len(param_def[i])):
        testlist[k].append(param_def[i][k])
        
group_identification = []
for i in range(len(testlist)):
    results = [0] * len(labels)
    for k in range(len(testlist[i])):
        if(testlist[i][k] == 1):
            results[0] +=1
        elif(testlist[i][k] == 2):
            results[1] +=1
        elif(testlist[i][k] == 3):
            results[2] +=1           
    
    group_identification.append(results.index(max(results))+1)
    
    
print(group_identification)



#Plot confusion matrix for overall fit
label = group_identification    
    
conf_mat = confusion_matrix(label, y_test)

fig = plt.figure(figsize=(3,3))
width = np.shape(conf_mat)[1]
height = np.shape(conf_mat)[0]

res = plt.imshow(np.array(conf_mat), cmap=plt.cm.summer, interpolation='nearest')
for i, row in enumerate(conf_mat):
    for j, c in enumerate(row):
        if c>0:
            plt.text(j-.2, i+.1, c, fontsize=16)
            
#cb = fig.colorbar(res)
plt.title('Confusion Matrix for Group Parameters')
plt.xlabel('Data')
plt.ylabel('ML Identification')
_ = plt.xticks(range(3), [l for l in labels.values()], rotation=90)
_ = plt.yticks(range(3), [l for l in labels.values()])

    
    
    
    
    
    
    
    
    
    