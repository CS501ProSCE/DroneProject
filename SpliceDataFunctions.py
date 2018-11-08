# CS 501 Group 16 Scrips of relevant funcitons #

from matplotlib import pyplot
import numpy as np

# get TS data from file
def getTSData(file_name):
    ts_data = []
    file = open(file_name,"r")
    for line in file:
        l = int(line)
        ts_data.append(l)
    file.close()
    return ts_data

# clean TS data at 400 and -400 threshold
# for other parameters:
#   should use user defined threshold
#   based on visual TS plot (idea is to get rid of noise)
def cleanTSData(ts_data):
    clean_data = []
    for i in range(len(ts_data)):
        if ts_data[i] < -400 or ts_data[i] > 400:
            clean_data.append(ts_data[i])
        else:
            clean_data.append(0)
    return clean_data

# creats an array of arrays containing only anomaly subsets of ts
def parseData(data):
    array = []
    firstZero = False
    newArray = []
    lengthThreashHold = 10
    zeroThreashHold = 5
    zeroCount = 0
    
    for i in range(len(data) -1):
        if data[i] == 0 and firstZero and zeroCount >= zeroThreashHold:
            if len(newArray) >= lengthThreashHold:
                newArray.append(0)
                array.append(newArray)
            newArray = [0]
            firstZero = False
            zeroCount = 0
        elif (data[i] != 0 and firstZero):
            newArray.append(data[i])
        elif data[i] != 0 and firstZero == False:
            firstZero = True
            newArray.append(data[i])
            zeroCount = 0
        elif data[i] == 0:
            zeroCount += 1
            
    if len(newArray) >= lengthThreashHold:
        newArray.append(0)
        array.append(newArray)
    return array

# goes through anomalies and creates each subset to be the same length
def anomLen(anom):
    lens = []
    for j in range(len(anom)):
        lens.append(len(anom[j]))
    max_len = max(lens)
    max_len_loc = lens.index(max(lens))
    for k in range(len(anom)):
        if len(anom[k]) < max_len:
            for l in range(max_len-len(anom[k])):
                anom[k].append(0)
    return anom

# basic plot of original time series data
def plotTSData(ts_data):
    pyplot.figure()
    pyplot.plot(ts_data)
    pyplot.show()

# need to save data in files or a way to use with learn.py

# example of main calling these funcitons in correct order    
def main():
    file_name = input("Name of CSV file:")
    ts_data = getTSData(file_name)
    clean_data = cleanTSData(ts_data)
    anom = parseData(clean_data)
    eq_anom = anomLen(anom)
    plotTSData(ts_data)

