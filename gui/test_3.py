"""
CS501 Group 16
Fall 2018
Modified/adapted from code baseline by Thomas Shaw

This module imports the data and executes the algorithms.

Re-used code from: https://github.com/markdregan/K-Nearest-Neighbors-with-Dynamic-Time-Warping
credit: Mark Dregan

*Some modifications made for implementation in Python3 and custom data input, plotting

"""
def learn(filename,param_list):
    import matplotlib.pyplot as plt
    import numpy as np

    from knndtw import KnnDtw
    from knndtw import ProgressBar

    # dataparam = 'mavlink_attitude_t_yaw angle'
    dataparam = filename

    trainingdatafile = 'Data/train_' + dataparam + '.txt'

    traininglabelfile = 'Data/train_labels.txt'



    # testdatafile = 'Data/test_' + dataparam + '.txt'
    # testdatafile = 'test_mavlink_x_gyro.txt'
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
    labels = {1: 'Hover', 2: 'Impact (tapping)', 3: 'Wind'}


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


    # Convert to numpy for efficiency
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    # y_test = np.array(y_test)

    plot2 = plt.figure("test_parameter: " + str(param_list[0])+" profile", figsize=(11, 7))
    colors = ['#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
              '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27', '#BCBD27', '#BCBD27', '#BCBD27', '#BCBD27',
              '#BCBD27', '#BCBD27', '#BCBD27', '#BCBD27', '#BCBD27', '#BCBD27', '#BCBD27', '#BCBD27', '#BCBD27',
              '#BCBD27', '#BCBD27', '#BCBD27', '#BCBD27', '#BCBD27']
    for i, r in enumerate ([i for i in range(len(x_test))]):
        plt.subplot(8, 2, i + 1)
        # plt.plot(x_test[r], label=labels[y_test[r]], color=colors[i], linewidth=2)
        plt.plot(x_test[r], color=colors[i], linewidth=2)
        plt.xlabel('Samples @50Hz')
        # plt.legend(loc='upper left')
        plt.tight_layout()
    plt.show()



learn("mavlink_raw_imu_t_XGyro",["hi"])







