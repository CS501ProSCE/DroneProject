"""
CS501 Group 16: Mission Planner Embedded Data Export
Author: Ryan Kelly

This is a simple script to capture data internal to Mission Planner (MP) using the current state (CS) class.
It's usage is detailed here: http://ardupilot.org/planner/docs/using-python-scripts-in-mission-planner.html

The data is captured at a user specified rate and written to a temporary file to be read later using the 
"MP_Embedded_RealTimeAnalayzer.py" script. A lower sample rate (20hz default) is used to allow faster calculation from 
kNN and DTW algorithm.
"""

import time
import csv

"""User defined variables """
sampleRate = 20.0 #in hz (recommend 20)
sampleLength = 2 #seconds
timeScale = int(sampleRate*sampleLength)

initialTime = int(round(time.time()*1000))

"""create the data file"""
i = 0

xGyro = ["xGyro"]
yGyro = ["yGyro"]
zGyro = ["zGyro"]
xAcc = ["xAcc"]
yAcc = ["yAcc"]
zAcc =["zAcc"]
pitch = ["pitch"]
roll = ["roll"]
yaw = ["yaw"]
navRoll = ["navRoll"]
navPitch = ["navPitch"]
navBearing = ["navBearing"]
channel1In = ["rollInput"] #roll input
channel2In = ["pitchInput"] #pitch input
channel3In = ["throttleInput"] # throttle input
channel4In = ["yawInput"] # yaw input
gpsTime = ["gpsTime"] #time stamp from GPS
time_ms = ["time(ms)"]
currentTime = int(round(time.time() * 1000))
print('Embedded Data Activated!')

"""main program: write data to file"""
while True:   
    currentTime = int(round(time.time() * 1000))
    time_ms.append(int(currentTime - initialTime))
    xGyro.append(cs.gx)
    yGyro.append(cs.gy)
    zGyro.append(cs.gz)
    xAcc.append(cs.ax)
    yAcc.append(cs.ay)
    zAcc.append(cs.az)
    pitch.append(cs.pitch)
    roll.append(cs.roll)
    yaw.append(cs.yaw)
    navRoll.append(cs.nav_roll) #roll command output from controller
    navPitch.append(cs.nav_pitch) #pitch command output from controller
    navBearing.append(cs.nav_bearing) #bearing command output from controller
    channel1In.append(cs.ch1in) #roll transmitter from input
    channel2In.append(cs.ch2in) #pitch input from transmitter
    channel3In.append(cs.ch3in) # throttle input from transmitter
    channel4In.append(cs.ch4in) # yaw input from transmitter 
    if len(time_ms) % (int(sampleRate)/2) == 0: #remainder determines when to write to temp file
        with open('EmbeddedDataTemp.csv', "wb") as dataFile:
            writer = csv.writer(dataFile)
            writer.writerow(time_ms[len(time_ms)-timeScale:])       
            writer.writerow(xGyro[len(time_ms)-timeScale:])
            writer.writerow(yGyro[len(time_ms)-timeScale:])
            writer.writerow(zGyro[len(time_ms)-timeScale:])
            writer.writerow(xAcc[len(time_ms)-timeScale:])
            writer.writerow(yAcc[len(time_ms)-timeScale:])
            writer.writerow(zAcc[len(time_ms)-timeScale:])
            writer.writerow(pitch[len(time_ms)-timeScale:])
            writer.writerow(roll[len(time_ms)-timeScale:])
            writer.writerow(yaw[len(time_ms)-timeScale:])
            writer.writerow(navRoll[len(time_ms)-timeScale:])
            writer.writerow(navPitch[len(time_ms)-timeScale:])
            writer.writerow(navBearing[len(time_ms)-timeScale:])
            writer.writerow(channel1In[len(time_ms)-timeScale:])
            writer.writerow(channel2In[len(time_ms)-timeScale:])
            writer.writerow(channel3In[len(time_ms)-timeScale:])
            writer.writerow(channel4In[len(time_ms)-timeScale:])
            #writer.writerow(time_ms)     
            print ('data write')
    time.sleep(1/sampleRate)
            

