"""
CS501 Group 16
Fall 2018
Modified/adapted from code baseline by Thomas Shaw

This module imports the data and executes the algorithms.

Re-used code from: https://github.com/markdregan/K-Nearest-Neighbors-with-Dynamic-Time-Warping
credit: Mark Dregan

*Some modifications made for implementation in Python3 and custom data input, plotting

"""
import math
import matplotlib.pyplot as plt
import numpy as np

from knndtw import KnnDtw
from knndtw import ProgressBar

def learn(filename):


    # dataparam = 'mavlink_attitude_t_yaw angle'
    dataparam = filename
    trainingdatafile = 'Data/train_' + dataparam + '.txt'
    traininglabelfile = 'Data/train_labels.txt'
    testdatafile = 'test_'+dataparam +'.txt'


    # testlabelfile = 'Data/test_labels.txt'

    # Import the HAR dataset
    x_train_file = open(trainingdatafile, 'r')
    y_train_file = open(traininglabelfile, 'r')

    x_test_file = open(testdatafile, 'r')
    # y_test_file = open(testlabelfile, 'r')

    # Create empty lists
    x_train = []
    y_train = []
    x_test = []
    # y_test = []

    # Mapping table for classes

    labels = {1: 'Hover', 2: 'Impact (Front Left)', 3: 'Impact (Front Right)', 4: 'Impact (Back Left)',
              5: 'Impact (Back Right)',
              6: 'Gust (from Left)', 7: 'Gust (from Right)', 8: 'Gust (from front)'}

    # Loop through datasets
    for x in x_train_file:
        x_train.append([float(ts) for ts in x.split()])


    for y in y_train_file:
        y_train.append(int(y.rstrip('\n')))


    for x in x_test_file:
        x_test.append([float(ts) for ts in x.split()])


    # for y in y_test_file:
        # y_test.append(int(y.rstrip('\n')))

    # close data files
    x_train_file.close()
    y_train_file.close()
    x_test_file.close()
    # y_test_file.close()
    print(x_test)


    # Convert to numpy for efficiency
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    # y_test = np.array(y_test)
    print(x_test)

    # Analyze dataset
    return x_test,x_train,y_train,labels

def machine_learning(x_test,x_train,y_train,labels):
    print (len(x_train))

    m = KnnDtw(n_neighbors=1, max_warping_window=100)
    m.fit(x_train, y_train)
    label, proba = m.predict(x_test)
    for i in label:
        print (labels[i])
    return label


    # Classification report
    # from sklearn.metrics import classification_report, confusion_matrix
    # print(classification_report(label, y_test,
    #                             target_names=[l for l in labels.values()]))

    # print(confusion_matrix(label, y_test))
    # plot1 = plt.figure("training_parameter: " + str(param_list[0])+" profile",figsize=(11, 7))
    # colors = ['#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
    #           '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
    #           '#D62728', '#2C9F2C', '#2C9F2C']
    # for i, r in enumerate([0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]):
    #     plt.subplot(7, 2, i + 1)
    #     plt.plot(x_train[r], label=labels[y_train[r]], color=colors[i], linewidth=2)
    #     plt.xlabel('Samples @50Hz')
    #     plt.legend(loc='upper left')
    #     plt.tight_layout()

def test_data_plot(param_list,x_test):
    plot2 = plt.figure("Test data profile (parameter: " + str(param_list[0]) + ")", figsize=(11, 7))



    colors = ['#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              ]
    for i, r in enumerate ([i for i in range(len(x_test))]):

        a= math.ceil(len(x_test)/2)

        plt.subplot(a, 2, i + 1)
        # plt.plot(x_test[r], label=labels[y_test[r]], color=colors[i], linewidth=2)
        plt.plot(x_test[r], color=colors[i], linewidth=2)
        plt.xlabel('Samples @50Hz')
        # plt.legend(loc='upper left')
        plt.tight_layout()
    plt.show()

def training_data_plot(param_list,x_train,y_train,labels):

    plot1 = plt.figure("Training data profile (parameter: " +  str(param_list[0]) + ")", figsize=(11, 7))

    colors = ['#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
                  '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
              '#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',


              ]

    for i, r in enumerate([i for i in range(len(x_train))]):
         a = math.ceil(len(x_train) / 2)

         plt.subplot(a, 2, i + 1)
         plt.plot(x_train[r], label=labels[y_train[r]], color=colors[i], linewidth=2)
         plt.xlabel('Samples @50Hz')
         plt.legend(loc='upper left')
         plt.tight_layout()
    plt.show()










    # def test_data_plot():
    #     # Plot Test data
    #     plot2 = plt.figure(figsize=(11, 7))
    #     colors = ['#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
    #               '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27','#BCBD27']
    #     for i, r in enumerate([0, 1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14]):
    #         plt.subplot(8, 2, i + 1)
    #         # plt.plot(x_test[r], label=labels[y_test[r]], color=colors[i], linewidth=2)
    #         plt.plot(x_test[r], color=colors[i], linewidth=2)
    #         plt.xlabel('Samples @50Hz')
    #         # plt.legend(loc='upper left')
    #         plt.tight_layout()
    #     plt.show()
    #
    # def confusion_matrix_plot():
    #     # Confusion Matrix
    #     conf_mat = confusion_matrix(label, y_test)
    #
    #     fig = plt.figure(figsize=(3, 3))
    #     width = np.shape(conf_mat)[1]
    #     height = np.shape(conf_mat)[0]
    #
    #     res = plt.imshow(np.array(conf_mat), cmap=plt.cm.summer, interpolation='nearest')
    #     for i, row in enumerate(conf_mat):
    #         for j, c in enumerate(row):
    #             if c > 0:
    #                 plt.text(j - .2, i + .1, c, fontsize=16)
    #
    #     plt.title('Confusion Matrix for ' + dataparam)
    #     plt.xlabel('Data')
    #     plt.ylabel('ML Identification')
    #     _ = plt.xticks(range(3), [l for l in labels.values()], rotation=90)
    #     _ = plt.yticks(range(3), [l for l in labels.values()])
    #     plt.show()
    #
    #
    #
    # # traning_data_plot()
    # # test_data_plot()

#
#
# x_test,x_train,y_train,labels=learn("mavlink_raw_imu_t_XGyro")
# machine_learning(x_test,x_train,y_train,labels)






