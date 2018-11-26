"""
CS501 Group 16
Fall 2018
Written by Thomas Shaw

This module imports the data and executes the algorithms.

ML algorithm re-used code from: https://github.com/markdregan/K-Nearest-Neighbors-with-Dynamic-Time-Warping
credit: Mark Dregan


"""


from MavlinkParameters import mavlink_types
from MavlinkParameters import mavlink_param
from MavlinkParameters import mavlink_index

import matplotlib.pyplot as plt
import numpy as np

from knndtw import KnnDtw
from knndtw import ProgressBar
from k_fold_cv import k_fold_cross_val

dataset = 'Data2/'
trainsample = 1 #this will choose how much to downsample training data. (1 = all data, 2 = half data, 4 = quarter data)

#get time for computatoin length
timestartalg = datetime.datetime.now()

#loop through entire parameter set, ignoring index 1 which is timestamp
for typ in range(1,len(mavlink_types)):
    for param in range(1,len(mavlink_param[typ])):
        
        dataparam = mavlink_types[typ] + '_' + mavlink_param[typ][param]
        
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
        labels = {1:'Hover', 2:'Impact (Front Left)', 3:'Impact (Front Right)', 4:'Impact (Back Left)', 5:'Impact (Back Right)', 
                  6:'Gust (from Left)', 7:'Gust (from Right)', 8: 'Gust (from front)' }
        
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
        
        
        #Analyze dataset
        m = KnnDtw(n_neighbors=3, max_warping_window=500)
        m.fit(x_train[::trainsample], y_train)
        label, proba = m.predict(x_test)
        
        #Classification report
        from sklearn.metrics import classification_report, confusion_matrix
        print(classification_report(label, y_test,
                                    target_names=[l for l in labels.values()]))
        
        
        #Confusion Matrix
        conf_mat = confusion_matrix(label, y_test)
        
        fig = plt.figure(figsize=(7,7))
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
        _ = plt.xticks(range(8), [l for l in labels.values()], rotation=90)
        _ = plt.yticks(range(8), [l for l in labels.values()])


#get end time for computatoin length and compute total run time
timeendalg = datetime.datetime.now()
runtime = timeendalg - timestartalg
print('total algorithm computation time was %f seconds' % (runtime.total_seconds()))


