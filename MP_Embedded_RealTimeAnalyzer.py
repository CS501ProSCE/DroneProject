"""
CS501 Group 16
Fall 2018

Mission Planner Embedded Real-Time Analyzer
Author: Ryan Kelly

This script reads temporary data from EmbeddedDataTemp.csv and does several things: 
    - Plots the live data to the top subplot of a matplotlib animated plot.
    - Uses a threshold to capture an "event", slice it, and display the most recent event on the the lower subplot.
    - Writes all the data to a file called "EmbeddedDataFull.csv" upon closing the matplotlib plot.
    - Writes an array of all sliced events to "EmbeddedDataImpacts.csv"
    - for all the above, the user can select which of (16) telemetry parameters to display, and all 16 parameters are written
        to both files.
    - Opens a seperate thread to process the most recent impact through the kNN/DTW classifier, without interfering
        with data capture rates.
        BR,BL,FL,FR
        time
time
xgyro
ygyro
zgyro
xacc
yacc
zacc
pitch
roll
yaw
navroll
navpitch
navbearing
rollinput
pitchinput
throttleinput


"""
import time
from threading import Thread
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv
#from multi_param_learn import multi_param_learn

os.chdir("C:\Program Files (x86)\Mission Planner")
style.use('fivethirtyeight')

fig = plt.figure()
plt.title("Live Data")
plt.xlabel("Time (ms)")
plt.ylabel("MP xGyro Data")
ax = fig.add_subplot(2,1,1)
bx = fig.add_subplot(2,1,2)
line, = ax.plot([], [])
eventList = [[]]
paramList = [["time(ms)"],["xGyro"],["yGyro"],["zGyro"],["xAcc"],["yAcc"],["zAcc"],["pitch"],["roll"],["yaw"],["navRoll"],["navPitch"],["navBearing"],["rollInput"],["pitchInput"],["throttleInput"]]
sampleRate = 20
thresholdSetting = 1500
impactCounter = 0
eventArray = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]] #zeros required for proper initializing

def animate(i): #this function is the main plotting loop, as well as other main functions of the program (like data gathering)
    data =[] #reset to empty
    with open('EmbeddedDataTemp.csv') as csvfile: #update the data
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            row = map(float, row) #convert to integer
            data.append(row)
    x = data[0]
    y = data[1]
    maxValue = max(y)
    if maxValue > 2000:
        maxIndex = y.index(maxValue)
        #print(maxValue)
        if 15 <= maxIndex <= 25: #This if statement controls what to plot on the subplot
            y1 = y[maxIndex-10:maxIndex+20]
            x1 = x[maxIndex-10:maxIndex+20]
            bx.clear()
            bx.plot(x1,y1)
            if eventArray[-16][0] != x1[0]: #this if statement writes to the eventArray (trimmed data)
                for i in range(0, len(paramList)):
                    data[i] = data[i][maxIndex-10:maxIndex+20]
                    eventArray.append(data[i])
                print("Event Detected...Classifying...")
            
    line.set_data(x, y)
    ax.clear()
    ax.plot(x, y)
    if paramList[0][-1] == "time(ms)" or paramList[0][-1]< data[0][0]: #Check to make sure it's not a duplicate time series
        for i in range(0,len(paramList)):
            paramList[i].extend(data[i]) #add the new time series to the full cumulative series#
    return line,

def handle_close(evt): #handler for closing the plot: Creates the full timeseries output file if needed for post analysis.
    print('Mission Planner Real_Time Analyzer Closed.')
    k=0
    while os.path.exists("EmbeddedDataFull%s.csv" %k):
        k += 1
    print("Full Data written to file: EmbeddedDataFull%s.csv" %k)
    with open('EmbeddedDataFull%s.csv' %k, "wb") as dataFile:
        writer = csv.writer(dataFile)
        for i in range (0,len(paramList)):
            writer.writerow(paramList[i])
    with open('EmbeddedDataImpacts%s.csv' %k, "wb") as dataFile2:
        writer = csv.writer(dataFile2)
        for i in range (0,len(eventArray)):
            writer.writerow(eventArray[i])
        
fig.canvas.mpl_connect('close_event', handle_close)

anim = animation.FuncAnimation(fig, animate, interval =250, blit=False)
plt.show()
print("Mission Planner Real-Time Analyzer Start!")

