"""
CS501 Group 16
Fall 2018
Modified/adapted from code baseline by Thomas Shaw

This module imports the data and executes the algorithms.

Re-used code from: https://github.com/markdregan/K-Nearest-Neighbors-with-Dynamic-Time-Warping
credit: Mark Dregan

*Some modifications made for implementation in Python3 and custom data input, plotting

"""
def learn(filename):
    import matplotlib.pyplot as plt
    import numpy as np

    from knndtw import KnnDtw
    from knndtw import ProgressBar

    # dataparam = 'mavlink_attitude_t_yaw angle'
    dataparam = filename

    trainingdatafile = 'Data/train_' + dataparam + '.txt'
    traininglabelfile = 'Data/train_labels.txt'

    # testdatafile = 'Data/test_' + dataparam + '.txt'
    # testlabelfile = 'Data/test_labels.txt'

    # Import the HAR dataset
    x_train_file = open(trainingdatafile, 'r')
    y_train_file = open(traininglabelfile, 'r')

    # x_test_file = open(testdatafile, 'r')
    # y_test_file = open(testlabelfile, 'r')

    # Create empty lists
    x_train = []
    y_train = []
    # x_test = []
    # y_test = []

    # Mapping table for classes
    labels = {1: 'Hover', 2: 'Impact (tapping)', 3: 'Wind'}

    # Loop through datasets
    for x in x_train_file:
        x_train.append([float(ts) for ts in x.split()])

    for y in y_train_file:
        y_train.append(int(y.rstrip('\n')))

    # for x in x_test_file:
    #     x_test.append([float(ts) for ts in x.split()])
    #
    # for y in y_test_file:
    #     y_test.append(int(y.rstrip('\n')))

    # close data files
    x_train_file.close()
    y_train_file.close()
    # x_test_file.close()
    # y_test_file.close()

    # Convert to numpy for efficiency
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    # x_test = np.array(x_test)
    # y_test = np.array(y_test)

    # Analyze dataset
    m = KnnDtw(n_neighbors=1, max_warping_window=100)
    m.fit(x_train, y_train)
    # label, proba = m.predict(x_test)  Result

    # Classification report
    # from sklearn.metrics import classification_report, confusion_matrix
    # print(classification_report(label, y_test,
    #                             target_names=[l for l in labels.values()]))
    #
    # print(confusion_matrix(label, y_test))


    def traning_data_plot():
        # plot train data
        plot1 = plt.figure(figsize=(11, 7))
        colors = ['#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
                  '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27',
                  '#D62728', '#2C9F2C']
        for i, r in enumerate([0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]):
            plt.subplot(7, 2, i + 1)
            plt.plot(x_train[r], label=labels[y_train[r]], color=colors[i], linewidth=2)
            plt.xlabel('Samples @50Hz')
            plt.legend(loc='upper left')
            plt.tight_layout()
        plt.show()
    return x_train,y_train


    # print (x_train)
    # print (y_train)
    # traning_data_plot()

    # def test_data_plot():
    #     # Plot Test data
    #     plot2 = plt.figure(figsize=(11, 7))
    #     colors = ['#D62728', '#2C9F2C', '#FD7F23', '#1F77B4', '#9467BD',
    #               '#8C564A', '#7F7F7F', '#1FBECF', '#E377C2', '#BCBD27']
    #     for i, r in enumerate([0, 1, 2, 3, 4, 5]):
    #         plt.subplot(3, 2, i + 1)
    #         plt.plot(x_test[r], label=labels[y_test[r]], color=colors[i], linewidth=2)
    #         plt.xlabel('Samples @50Hz')
    #         plt.legend(loc='upper left')
    #         plt.tight_layout()
    #     plt.show()

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







