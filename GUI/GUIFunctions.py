"""
CS 50100 Group 16
Written by Ashley Dicks
Script to be used with GUI for mavlink UAV data to be analyized
By:
1. Extract raw drone data from Mission Planner output
2. Be able to user specify the parameter
3. Create a new data array with only this parameter
4. Use the automatic splice method to detect disturbances
5. Run the unlabled disturbances through the ML algorithm to lable
Functions:
* csvParaExtract():
* plotParaData():
*
"""

from autoSpliceClass import AnomalyDetection
from matplotlib import pyplot
import math
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
import matplotlib.patches as mpatches

import numpy as np
import datetime
import os
import random ## for fake labels ##

# import mavlink parameter format
from MavlinkParameters import mavlink_types
from MavlinkParameters import mavlink_param
from MavlinkParameters import mavlink_index
from MavlinkParameters import mavlink_rate
## RAW DATA EXTRACTION FUNCTIONS ##

# function to create time series for flight of specified paramter
def csvParaExtract(file_name,para_name):
    # Create Data
    mavlink_data = []
    for typ in range(len(mavlink_types)):
        typdata = []
        for _ in range(len(mavlink_param[typ])):
            typdata.append([])
        mavlink_data.append(typdata)

    #read raw data file
    filelist = []
    with open(file_name) as f:
        for line in f:
            filelist.append(line.split(','))
    f.close()
    print("Generating time series for "+para_name+" from file "+file_name)
    # read all data from file into parameter lists
    for row in filelist:
        for typ in range(len(mavlink_types)):
            if (str(row[9]) == mavlink_types[typ]):
                for param in range(len(mavlink_param[typ])):
                    if(param==0):
                        mavlink_data[typ][param].append(row[mavlink_index[typ][param]-1])
                    else:
                        mavlink_data[typ][param].append(float(row[mavlink_index[typ][param]-1]))
    data = []
    count = 0
    for typ in range(len(mavlink_types)):
        for param in range(len(mavlink_param[typ])):
            if mavlink_param[typ][param] == para_name:
                if count == 0:
                    for i in range(len(mavlink_data[typ][param])):
                        data.append(mavlink_data[typ][param][i])
                    rate = mavlink_rate[typ]
                    count = count + 1
                    mav_type = mavlink_types[typ]

    print("Done collecting "+para_name+" data!")
    return data,rate,mav_type

# funciton to plot specified parameter time series data
def plotParaData(data):
    pyplot.figure(1)
    pyplot.plot(data)
    pyplot.show()


## SPLICING FUNCTIONS ##

# manually select individual anomalies from TS data
def manParseData(data,name):
    x_pts = []
    y_pts = []
    fig, ax = pyplot.subplots(figsize=(15, 7))
    ax.plot(data)
    pyplot.title("Complete Time Series (Parameter: "+ name+")", size=20)
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
    return anoms, index_x,x_pts
def manParseData2(data,x_pts):

    index_x = [int(x_pts[i]) for i in range(len(x_pts))]
    anoms = []
    # create n new array for anamoly ts from dataset
    for i in range(0, len(index_x) - 1):
        # x_pts are where anomalies begin and end
        start = index_x[i]
        end = index_x[i + 1]
        anoms.append(data[start:end])
    return anoms, index_x


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


def parseData(data,index_x):

    anoms = []

    for i in range(0,len(index_x)-1,2):

        start = index_x[i]

        end = index_x[i+1]

        anoms.append(data[start:end])

    return anoms, index_x

# creats an array of arrays containing only anomaly subsets of ts
# def parseData(data):
#     array = []
#     firstZero = False
#     newArray = []
#     lengthThreashHold = 10
#     zeroThreashHold = 5
#     zeroCount = 0
#
#     for i in range(len(data) - 1):
#         if data[i] == 0 and firstZero and zeroCount >= zeroThreashHold:
#             if len(newArray) >= lengthThreashHold:
#                 newArray.append(0)
#                 array.append(newArray)
#             newArray = [0]
#             firstZero = False
#             zeroCount = 0
#         elif (data[i] != 0 and firstZero):
#             newArray.append(data[i])
#         elif data[i] != 0 and firstZero == False:
#             firstZero = True
#             newArray.append(data[i])
#             zeroCount = 0
#         elif data[i] == 0:
#             zeroCount += 1
#
#     if len(newArray) >= lengthThreashHold:
#         newArray.append(0)
#         array.append(newArray)
#     return array

# goes through anomalies and creates each subset to be the same length
def anomLen(anom,rate):
    lens = []
    desire_len = int(rate*6)
    if desire_len%2!=0:
        desire_len=desire_len+1
    # print (desire_len)
    mean = 0


    for j in range(len(anom)):
        if anom[j] == []:
            pass
        else:
            mean = mean + sum(anom[j]) / len(anom[j])
    ts_mean = mean / len(anom)
    lens.append(len(anom[j]))
    # print("mean:", ts_mean)
    max_len = desire_len # max(lens)
    for k in range(len(anom)):


        if len(anom[k]) <= max_len:

            for l in range(len(anom[k]), max_len):
                anom[k].append(ts_mean)
            # print ("1",anom[k])

            min_num1 = int(anom[k].index(max(anom[k])) - max_len / 2)
            max_num1 = int(anom[k].index(max(anom[k])) + max_len / 2)

            if min_num1 < 0:

                for l in range(0, math.ceil(max_len / 2 - anom[k].index(max(anom[k]))) - 1):
                    anom[k].insert(0, ts_mean)

                anom[k] = anom[k][0:max_len]

            else:

                for l in range(0, math.ceil(anom[k].index(max(anom[k])) - max_len / 2)):
                    anom[k].append(ts_mean)
                    # anom[k].remove(anom[k][0])

                anom[k] = anom[k][min_num1:max_num1]
            # print("2",anom[k])

        if len(anom[k]) > max_len:
            # print ("3")

            min_num2 = int(anom[k].index(max(anom[k])) - max_len / 2)
            max_num2 = int(anom[k].index(max(anom[k])) + max_len / 2)

            if min_num2 < 0:
                for l in range(0, math.ceil(max_len / 2 - anom[k].index(max(anom[k]))) - 1):
                    anom[k].insert(0, ts_mean)

                anom[k] = anom[k][0:max_len]

            elif max_num2 > len(anom[k]):
                for l in range(0, int(max_len / 2) - len(anom[k]) + anom[k].index(max(anom[k])) + 1):
                    anom[k].insert(len(anom[k]), ts_mean)
                anom[k] = anom[k][min_num2 + 1:len(anom[k])]
            else:
                anom[k] = anom[k][min_num2:max_num2]


    # lens = []
    # desire_len = int(rate*6)
    # for j in range(len(anom)):
    #     lens.append(len(anom[j]))
    # max_len = desire_len # max(lens)
    # max_len_loc = lens.index(max(lens))
    # for k in range(len(anom)):
    #     if len(anom[k]) < max_len:
    #         for l in range(int((max_len - len(anom[k]))/2)):
    #             anom[k].append(0)
    # #             anom[k].insert(0,0)
    # for k in range(len(anom)):
    #     if len(anom[k]) < max_len:
    #         for l in range(len(anom[k]), max_len):
    #             anom[k].append(0)
    #             # anom[k].insert(0,0)
    #     else:
    #         for l in range (max_len,len(anom[k])):
    #             anom[k].remove(anom[k][max_len])
    return anom

# save anomalies to .txt files - to be used for learning algorithm
def saveAnom(para_name, eq_anom, mav_type):
    # print("eq_anom1:",eq_anom)
    filename = "test_" + str(mav_type) + "_" + str(para_name) + ".txt"
    if os.path.exists(filename):
        os.remove(filename)  # remove if already exists
    file = open(filename, 'w')
    for i in range(len(eq_anom)):
        file.write(' '.join(map(str, eq_anom[i])))
        file.write("\n")
    file.close()
    print("Disturbances successfully saved as: " + filename)

    return str(para_name)

## LABEL ANALYSIS PLOTS/ FIGURES ##

# basic plot of original time series data
def plotTSData(ts_data,paraname):

    pyplot.figure("Test data time series (parameter: "+ paraname+")")
    pyplot.plot(ts_data)
    pyplot.show()


# plot with disturbance type
def distLabel(data, index_x, labels, para_name):
    colors = [ "red", "firebrick","orange","yellow","blue","navy","royalblue"]
    # colors = ["green", "red", "firebrick","orange","yellow","blue","navy","royalblue"]


    colored_data = []
    for i in range(len(labels)):
        # if labels[i] == 1:
        #     colored_data.append(colors[0])
        if labels[i] == 2:
            colored_data.append(colors[0])
        elif labels[i] == 3:
            colored_data.append(colors[1])
        elif labels[i] == 4:
            colored_data.append(colors[2])
        elif labels[i] == 5:
            colored_data.append(colors[3])
        elif labels[i] == 6:
            colored_data.append(colors[4])
        elif labels[i] == 7:
            colored_data.append(colors[5])
        else:
            colored_data.append(colors[6])

    # append end of TS color and x_val
    index_x.append(len(data))
    colored_data.append("black")

    # legend info
    red_patch = mpatches.Patch(color='red', label=' Impact (Front Left)')
    # green_patch = mpatches.Patch(color='green', label='Hover')
    blue_patch = mpatches.Patch(color='blue', label='Gust (from Left)')
    firebrick_patch = mpatches.Patch(color='firebrick', label='Impact (Front Right)')
    navy_patch = mpatches.Patch(color='navy', label='Gust (from Right)')
    orange_patch = mpatches.Patch(color='orange', label='Impact (Back Left)')
    yellow_patch = mpatches.Patch(color='yellow', label='Impact (Back Right)')
    royalblue_patch = mpatches.Patch(color='royalblue', label='Gust (from front)')


    # plot
    fig, ax = pyplot.subplots(figsize=(15, 7))
    ax.plot(data)
    pp = pyplot.plot(data[0:index_x[0]], c="black")
    fig.canvas.draw()
    for j in range(0, len(index_x) - 1):
        x_vals = []
        for k in range(index_x[j], index_x[j + 1]):
            x_vals.append(k)
        line, = ax.plot(x_vals, data[index_x[j]:index_x[j + 1]], c=colored_data[j])
        # pt, = ax.plot(x_vals[0],0,c="black",marker="o",markersize=6)
        fig.canvas.draw()
    # pyplot.legend(handles=[green_patch,royalblue_patch,blue_patch,navy_patch,orange_patch, red_patch,firebrick_patch,yellow_patch])
    pyplot.legend(handles=[royalblue_patch,blue_patch,navy_patch,orange_patch, red_patch,firebrick_patch,yellow_patch])
    pyplot.title("Prediction result with parameter ("+str(para_name) + ")", size=24)
    pyplot.xlabel("Time", size=12)
    pyplot.ylabel(str(para_name), size=12)
    pyplot.show()

def distLabelAuto(data,index_x,labels,para_name):
    colors = [ "red", "firebrick", "orange", "yellow", "blue", "navy", "royalblue"]
    # colors = ["green", "red", "firebrick", "orange", "yellow", "blue", "navy", "royalblue"]

    colored_data = []
    for i in range(len(labels)):
        # if labels[i] == 1:
        #     colored_data.append(colors[0])
        if labels[i] == 2:
            colored_data.append(colors[0])
        elif labels[i] == 3:
            colored_data.append(colors[1])
        elif labels[i] == 4:
            colored_data.append(colors[2])
        elif labels[i] == 5:
            colored_data.append(colors[3])
        elif labels[i] == 6:
            colored_data.append(colors[4])
        elif labels[i] == 7:
            colored_data.append(colors[5])
        else:
            colored_data.append(colors[6])


    # append end of TS color and x_val
    index_x.append(len(data))
    colored_data.append("black")

    # legend info
    red_patch = mpatches.Patch(color='red', label=' Impact (Front Left)')
    # green_patch = mpatches.Patch(color='green', label='Hover')
    blue_patch = mpatches.Patch(color='blue', label='Gust (from Left)')
    firebrick_patch = mpatches.Patch(color='firebrick', label='Impact (Front Right)')
    navy_patch = mpatches.Patch(color='navy', label='Gust (from Right)')
    orange_patch = mpatches.Patch(color='orange', label='Impact (Back Left)')
    yellow_patch = mpatches.Patch(color='yellow', label='Impact (Back Right)')
    royalblue_patch = mpatches.Patch(color='royalblue', label='Gust (from front)')


    # plot
    fig, ax = pyplot.subplots(figsize=(15, 7))
    ax.plot(data)
    pp = pyplot.plot(data[0:index_x[0]],c="black")
    fig.canvas.draw()


    for j in range(0,len(index_x)-1,2):
        x_vals = []
        x_vals_off =[]
        for k in range(index_x[j],index_x[j+1]):
            x_vals.append(k)
        for l in range(index_x[j+1],index_x[j+2]):
            x_vals_off.append(l)
        line, = ax.plot(x_vals,data[index_x[j]:index_x[j+1]],c=colored_data[int(j/2)])
        line, = ax.plot(x_vals_off, data[index_x[j+1]:index_x[j+2]],c="black")
        #pt, = ax.plot(x_vals[0],0,c="black",marker="o",markersize=6)
        fig.canvas.draw()
    pyplot.legend(handles=[royalblue_patch,blue_patch,navy_patch,orange_patch, red_patch,firebrick_patch,yellow_patch])
    # pyplot.legend(handles=[green_patch,royalblue_patch,blue_patch,navy_patch,orange_patch, red_patch,firebrick_patch,yellow_patch])
    pyplot.title("Prediction result with parameter ("+str(para_name) + ")", size=24)
    pyplot.xlabel("Time",size=12)
    pyplot.ylabel(str(para_name),size=12)
    pyplot.show()



# MAIN FOR GUI
def main(file,paraname,paraname_readable):


    # FROM GUI INPUT
    file_name=file
    para_name =paraname

    data,rate,mav_type = csvParaExtract(file_name,para_name)

    anom,index_x,xpts = manParseData(data, paraname_readable)  ## EXAMPLE for manual anomaly selection

    eq_anom = anomLen(anom,rate)

    # saveAnom(para_name, eq_anom, mav_type)

    return data,index_x,para_name,xpts,eq_anom

def main2(file,paraname):

    file_name=file
    para_name =paraname

    data,rate,mav_type = csvParaExtract(file_name,para_name)

    anomalyDetection = AnomalyDetection(data)  ## EXAMPLE for automatic anomaly selection
    anom,index_x = anomalyDetection.parseData()
    eq_anom = anomLen(anom,rate)

    eq_anom = anomLen(anom,rate)
    # saveAnom(para_name, eq_anom, mav_type)
    return data, index_x, para_name, eq_anom

def main3(file,paraname,xpts):

    file_name=file
    para_name =paraname

    data,rate,mav_type = csvParaExtract(file_name,para_name)

    anom,index_x = manParseData2(data, xpts)  ## EXAMPLE for manual anomaly selection
    # print (xpts)
    # print (data)
    # print (anom)
    # print (index_x)
    # for x in range(len(anom)):
    #     print ("x: ",anom[x])

    eq_anom = anomLen(anom,rate)

    # saveAnom(para_name, eq_anom, mav_type)
    return eq_anom


# main2('2018-10-07 13-49-59.csv','XGyro',"X Gyro")

# main("2018-11-17 12-37-40.csv",'YGyro','Y Gyro')

def main4(file,paraname,index_x):



    file_name = file

    para_name = paraname

    data, rate, mav_type = csvParaExtract(file_name, para_name)

    anom, index_x = parseData(data, index_x)

    eq_anom = anomLen(anom,rate)

    # saveAnom(para_name, eq_anom, mav_type)
    return eq_anom
