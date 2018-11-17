# CS 501 Group 16 Scrips of relevant funcitons #
# Ashley Dicks

from matplotlib import pyplot
import numpy as np
import datetime
import os


# get TS data from file
def getTSData(file_name):
    ts_data = []
    file = open(file_name, "r")
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

    for i in range(len(data) - 1):
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


# manually select individual anomalies from TS data
def manParseData(data):
    x_pts = []
    y_pts = []
    fig, ax = pyplot.subplots(figsize=(15, 7))
    ax.plot(data)
    pyplot.title("Time Series for UAV Anomalies", size=20)
    txt = "INSTRUCTIONS: Click on points inbetween each anomaly viewed, starting at the front of the first anomaly and ending at the end of the last anomaly. EXIT when done! "
    fig.text(.5, .05, txt, ha='center')
    line, = ax.plot(x_pts, y_pts, marker="o")

    # function used for manual selection
    def onpick(event):
        m_x, m_y = event.x, event.y
        x, y = ax.transData.inverted().transform([m_x, m_y])
        x_pts.append(x)
        y_pts.append(y)
        line.set_xdata(x_pts)
        line.set_ydata(y_pts)
        fig.canvas.draw()

    fig.canvas.mpl_connect('button_press_event', onpick)
    pyplot.show()
    index_x = [int(x_pts[i]) for i in range(len(x_pts))]
    anoms = []
    # create n new array for anamoly ts from dataset
    for i in range(0, len(index_x) - 1):
        # x_pts are where anomalies begin and end
        start = index_x[i]
        end = index_x[i + 1]
        anoms.append(data[start:end])
    return anoms


# goes through anomalies and creates each subset to be the same length
def anomLen(anom):
    lens = []
    for j in range(len(anom)):
        lens.append(len(anom[j]))
    max_len = max(lens)
    max_len_loc = lens.index(max(lens))
    for k in range(len(anom)):
        if len(anom[k]) < max_len:
            for l in range(max_len - len(anom[k])):
                anom[k].append(0)
    return anom


# basic plot of original time series data
def plotTSData(ts_data,paraname):
    pyplot.figure("test_parameter: " + paraname+" complete profile")
    pyplot.plot(ts_data)
    # print("**")
    pyplot.show()



# need to save data in files or a way to use with learn.py
def saveAnom(para_name, eq_anom):
    # param_name = file_name[:-4] # remove the .csv from name (switched to user specify para name)
    filename = "test_" + str(para_name) + ".txt"
    if os.path.exists(filename):
        os.remove(filename)  # remove if already exists
    file = open(filename, 'w')
    for i in range(len(eq_anom)):
        file.write(' '.join(map(str, eq_anom[i])))
        file.write("\n")
    file.close()
    print("Disturbances successfully saved as: " + filename)
    return str(para_name)



# example of main calling these funcitons in correct order
def main(file,paraname,paraname_readable):
    # file_name = input("Name of CSV file:")  # tap_front_left_xgyro.csv
    file_name=file
    # file_name = "testData_raw_file1.csv"
    # para_name = input("Name of parameter to be used:")
    # para_name = "x_gyro"
    para_name = paraname

    ts_data = getTSData(file_name)
    # print (ts_data)
    clean_data = cleanTSData(ts_data)
    anom = parseData(clean_data) ## EXAMPLE for automatic
    # anom = manParseData(clean_data)  ## EXAMPLE for manual anomaly selection
    eq_anom = anomLen(anom)
    # plotTSData(ts_data,paraname_readable)

    return saveAnom(para_name, eq_anom)


