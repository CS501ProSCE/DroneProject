"""
CS501 Group 16
Fall 2018
Author: Jeff Xie
Credit: KFold implementation from sk.learn
Inputs:
    k_list: a list of k values for knn
    train: training data to be folded for cross validation
    label: labels for the training data
    folds: 
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import copy #for deepcopy, 
from knndtw import KnnDtw
from sklearn.model_selection import KFold
#Import scoring metrics, import more as needed
from sklearn.metrics import classification_report, confusion_matrix, precision_score, accuracy_score


def k_fold_cross_val(k_list,train,label,folds):
    #Randomly shuffle the data and label in to the same sequence 
    seed = np.arange(train.shape[0])
    np.random.shuffle(seed)
    train = train[seed]
    label = label[seed]
    #Keep track of the score for this k value, num of scores = num of folds
    k_scores = [] #averaged scores for each k value, num of scores = num of K
    
    #we want to split train data into test and train
    label_name = {1:'Hover', 2:'Impact (tapping)', 3:'Wind'}
    clf = KnnDtw(n_neighbors=1, max_warping_window=100) #Initialize classifier
    kf = KFold(n_splits=folds)
    kf.get_n_splits(train)
    for K in k_list:
        scores = [] #averaged scores for each k value, num of scores = num of K
        clf = KnnDtw(n_neighbors=K, max_warping_window=100)
        for train_index, test_index in kf.split(train):
            print("TRAIN:", train_index, "TEST:", test_index)
            X_train, X_test = train[train_index], train[test_index]
            y_train, y_test = label[train_index], label[test_index]
            clf_copy = copy.deepcopy(clf) #try to make sure the estimator is reset before each fit, but maybe I can just move clf into the loop?
            clf_copy.fit(X_train,y_train)
            labels, proba = clf_copy.predict(X_test)
            #print(classification_report(labels, y_test,target_names=[l for l in label_name.values()]))
            acc = accuracy_score(y_test,labels)
            print('Accuracy for this fold is:', acc)
            scores.append(acc)
        scores = np.array(scores) #convert the fold scores array into numpy
        score = np.average(scores) #averages the fold scores to a single socre for the k 
        k_scores.append(score)
    #Plot the average accuracy score for each k, recommend a besk (highest accuracy) k
    plt.bar(k_list, k_scores,width=0.5)
    plt.xlabel('k (nearest neighbors)')
    plt.ylabel('Accuracy (average)')
    print('Best k value from list is:',k_list[np.argmax(k_scores)])