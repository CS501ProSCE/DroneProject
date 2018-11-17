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

from matplotlib import pyplot
import numpy as np
import datetime
import os

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
    for typ in range(len(mavlink_types)):
        for param in range(len(mavlink_param[typ])):
            if mavlink_param[typ][param] == para_name:
                for i in range(len(mavlink_data[typ][param])):
                    data.append(mavlink_data[typ][param][i])
                rate = mavlink_rate[typ]
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

# goes through anomalies and creates each subset to be the same length
def anomLen(anom,rate):
    lens = []
    desire_len = int(rate*6)
    for j in range(len(anom)):
        lens.append(len(anom[j]))
    max_len = desire_len # max(lens)
    # max_len_loc = lens.index(max(lens))
    # for k in range(len(anom)):
    #     if len(anom[k]) < max_len:
    #         for l in range(int((max_len - len(anom[k]))/2)):
    #             anom[k].append(0)
    #             anom[k].insert(0,0)
    for k in range(len(anom)):
        if len(anom[k]) < max_len:
            for l in range(len(anom[k]), max_len):
                anom[k].append(0)
                # anom[k].insert(0,0)
        else:
            for l in range (max_len,len(anom[k])):
                anom[k].remove(anom[k][max_len])
    return anom

# save anomalies to .txt files - to be used for learning algorithm 
def saveAnom(para_name, eq_anom, mav_type):
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



# MAIN FOR GUI
def main(file,paraname,paraname_readable):
    # *** Parameter to be specified by GUI ***
    # *** File to be specified by GUI ***
    # parameter = input("define which parameter to analyze: ") # XGyro
    # file = input("define Mavlink CSV file to use: ") # 2018-11-10 09-33-57.csv
    # data = csvParaExtract(file,parameter)

    # FROM GUI INPUT
    file_name=file
    para_name =paraname

    data,rate,mav_type = csvParaExtract(file_name,para_name)
    #clean_data = cleanTSData(ts_data)
    #anom = parseData(clean_data) ## EXAMPLE for automatic
    anom,index_x = manParseData(data, paraname_readable)  ## EXAMPLE for manual anomaly selection
    eq_anom = anomLen(anom,rate)
    print (eq_anom)
    # plotTSData(data,paraname_readable)
    saveAnom(para_name, eq_anom, mav_type)

    # return saveAnom(para_name, eq_anom, mav_type)
# main('2018-10-07 13-49-59.csv','XGyro',"X Gyro")
# main("/Users/lemo/PycharmProjects/droneGUI copy/2018-10-07 13-59-17.csv",'YGyro','Y Gyro')

