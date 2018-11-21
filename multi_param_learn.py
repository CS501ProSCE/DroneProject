"""
CS501 Group 16
Fall 2018
Modified/adapted from code baseline by Thomas Shaw, Jeff Xie

This module imports the data and executes the algorithms.

Inputs:
    para_list: a list of parameters to train and test the data, parameters are in string
    param_weight: a list of weights corresponding to parameters, used for aggregating 
    

Re-used code from: https://github.com/markdregan/K-Nearest-Neighbors-with-Dynamic-Time-Warping
credit: Mark Dregan

*Some modifications made for implementation in Python3 and custom data input, plotting

"""


import matplotlib.pyplot as plt
import numpy as np

from knndtw import KnnDtw
from knndtw import ProgressBar
from scipy import stats

from k_fold_cv import k_fold_cross_val



"let's try to create a feature vector with multiple parameters"
def multi_param_learn(param_list,param_weights,datapath):
    
    
    #this is the list that will store labels returned from each param before aggregating 
    param_labels = []
    if param_weights != None:
        if len(param_list) != len(param_weights):
            raise Exception('When using weights, there must one weight for each parameter!')
        para_weights = dict(zip(param_list,param_weights))
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
    
        ##plot train data
        #plt.figure(figsize=(11,7))
        #colors = ['#D62728','#2C9F2C','#FD7F23','#1F77B4','#9467BD',
        #          '#8C564A','#7F7F7F','#1FBECF','#E377C2','#BCBD27',
        #          '#D62728','#2C9F2C']
        #for i, r in enumerate([0,1,2,3,5,6,7,8,9,10,11,12]):
        #    plt.subplot(7,2,i+1)
        #    plt.plot(x_train[r], label=labels[y_train[r]], color=colors[i], linewidth=2)
        #    plt.xlabel('Samples @50Hz')
        #    plt.legend(loc='upper left')
        #    plt.tight_layout()
        #
        ##Plot Test data
        #plt.figure(figsize=(11,7))
        #colors = ['#D62728','#2C9F2C','#FD7F23','#1F77B4','#9467BD',
        #          '#8C564A','#7F7F7F','#1FBECF','#E377C2','#BCBD27']
        #for i, r in enumerate([0,1,2,3,4,5]):
        #    plt.subplot(3,2,i+1)
        #    plt.plot(x_test[r], label=labels[y_test[r]], color=colors[i], linewidth=2)
        #    plt.xlabel('Samples @50Hz')
        #    plt.legend(loc='upper left')
        #    plt.tight_layout()
        
        #Analyze dataset
        m = KnnDtw(n_neighbors=3, max_warping_window=100)
        m.fit(x_train, y_train)
        label, proba = m.predict(x_test)
        #get the weight for this parameter
        if param_weights == None:
            param_labels.append(label) #if we don't have weights do this
        else:
            weight = [para_weights[dataparam]]
            param_labels.append(list(zip(label,weight*len(label))))#a tuple list of (label, weight)
        
        
    param_labels = np.array(param_labels)
    if param_weights == None:
        para_mode, para_count = stats.mode(param_labels)
        para_mode = np.reshape(para_mode,(para_mode.shape[1],))
    else: #for weights
        para_mode = [0]*param_labels.shape[1]
        for i in range(param_labels.shape[1]):
            mode_count = [0]*len(labels) #an array representing how frequent each label was used to classify a time series
            col = param_labels[:,i]
            for p in col:
                mode_count[p[0]-1] += p[1]
            para_mode[i] = mode_count.index(max(mode_count)) + 1 #the the label that was used most frequently as the overall label
            #para_mode = np.reshape(para_mode,(para_mode.shape[1],))
        
    #Using mode to see which classification was the most frequent for each data from all parameters used
    #k_val = list(range(1,11))
    #k_fold_cross_val(k_val,x_train,y_train,6)
        
    
    #Classification report
    """ASSUMPTION: 
        We're trying to see accuracy of labelling as a result of multi param voting, but 
        we are only comparing to one y_test belonging to one (last) parameter with the current implementation
        we're assuming that y_test is the same across all param which builds on the assumption that
        train/test data for all param are from the same time period!
    """
    from sklearn.metrics import classification_report, confusion_matrix
    print(classification_report(para_mode, y_test,
                                target_names=[l for l in labels.values()]))
    
    
    #Confusion Matrix
    conf_mat = confusion_matrix(para_mode, y_test)
    
    fig = plt.figure(figsize=(8,8))
    width = np.shape(conf_mat)[1]
    height = np.shape(conf_mat)[0]
    
    res = plt.imshow(np.array(conf_mat), cmap=plt.cm.summer, interpolation='nearest')
    for i, row in enumerate(conf_mat):
        for j, c in enumerate(row):
            if c>0:
                plt.text(j-.2, i+.1, c, fontsize=16)
                    
    #cb = fig.colorbar(res)
    plt.title('Confusion Matrix for ' + ', '.join([name for name in param_list]))
    plt.xlabel('Data')
    plt.ylabel('ML Identification')
    _ = plt.xticks(range(9), [l for l in labels.values()], rotation=90)
    _ = plt.yticks(range(9), [l for l in labels.values()])
#testing
plist = ['mavlink_raw_imu_t_Zaccel']#,'mavlink_raw_imu_t_Zaccel']
#pw = [5,4]

multi_param_learn(plist,None,'Data2/')