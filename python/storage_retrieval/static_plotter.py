#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

with open("patient_z_graph_110917.txt", "r") as f:
 #graphData = f.read()
 graphData = f.readline()
 graphList = [i for i in graphData.split(',') if i!='\n']
 print(graphList)

fig, ax = plt.subplots()
ax.set_title("Patient Z Record - Heart Rate Waveform")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
plt.subplots_adjust(bottom=0.25)

#x = np.arange(0.0, 100.0, 0.1)
#x = range(0,100,1)
#y = np.sin(x)
#l = plt.plot(x,y)
x = range(0,len(graphList),1)
y = graphList
l = plt.plot(x,y)
plt.axis([0, 50, 0, 500])

axcolor = 'lightgoldenrodyellow'
axpos = plt.axes([0.2, 0.1, 0.65, 0.03], axisbg=axcolor)

spos = Slider(axpos, 'Pos', 0, len(graphList))

def update(val):
    pos = spos.val
    ax.axis([pos,pos+50,0,500])
    fig.canvas.draw_idle()

spos.on_changed(update)

plt.show()
