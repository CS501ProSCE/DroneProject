# -*- coding: utf-8 -*-
# DATA Splice using matplotlib
from matplotlib import pyplot
import numpy as np

def get_data(file_name):
    # get data from TS file
    xgyro_data = []
    file = open(file_name, "r")
    for line in file:
        l = int(line)
        xgyro_data.append(l)
    file.close()
    # threshold anomaly at 400 and -400
    clean_data = []
    for i in range(len(xgyro_data)):
        if xgyro_data[i] < -400 or xgyro_data[i] > 400:
            clean_data.append(xgyro_data[i])
        else:
            clean_data.append(0)

    x_pts = []
    y_pts = []

    fig, ax = pyplot.subplots(figsize=(15, 7))
    ax.plot(clean_data)
    pyplot.title("Time Series for UAV Anomalies", size=20)
    txt = "INSTRUCTIONS: Click on points inbetween each anomaly viewed, starting at the front of the first anomaly and ending at the end of the last anomaly. EXIT when done! "
    fig.text(.5, .05, txt, ha='center')
    line, = ax.plot(x_pts, y_pts, marker="o")

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

    # location array: loca[0] to loca[1] is anomaly 1
    #                 loca[1] to loca[2] is anomaly 2 .. etc
    index_x = [int(x_pts[i]) for i in range(len(x_pts))]
    anoms = []
    # create n new array for anamoly ts from dataset
    for i in range(0, len(index_x) - 1):
        # x_pts are where anomalies begin and end
        start = index_x[i]
        end = index_x[i + 1]
        anoms.append(xgyro_data[start:end])

    # pyplot.plot(anoms[0])
    # pyplot.show()

    # make all array's the same length:
    # find longest array (max(len(anom1))
    # add 0s to the shorter array ends to get all equal lengths
    lens = []
    for j in range(len(anoms)):
        lens.append(len(anoms[j]))

    max_len = max(lens)
    max_len_loc = lens.index(max(lens))

    # anom_same_len = []
    for k in range(len(anoms)):
        if len(anoms[k]) < max_len:
            for l in range(max_len - len(anoms[k])):
                anoms[k].append(0)

    # check to make sure lengths are all the same now
    lens2 = []
    for j in range(len(anoms)):
        lens2.append(len(anoms[j]))
    print(lens2)

    # plot anomalies separately
    for m in range(len(anoms)):
        pyplot.figure(m)
        pyplot.plot(anoms[m])
    pyplot.show()



def hello():
    print ("hello, this is a call test")

    # save anomalies in excel or csv: ask ryan and tom

# Ashley can test with following codes:
#get_data(file_name):