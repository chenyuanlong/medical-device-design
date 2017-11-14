#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
try:
 with open(root.filename, "r") as f:
  #graphData = f.read()
  graphData = f.readline()
  graphList = [i for i in graphData.split(',') if i!='\n' and i!='']
  name = root.filename.split('/')[-1].split('_')[0]
  timestamp = "Timestamp: " + root.filename.split('/')[-1].split('_')[-1][0:-4]
except :
 root.destroy()

def handle_close(evt):
 global root,timestamp
 root.destroy()
fig, ax = plt.subplots()
fig.canvas.set_window_title('LLG Heart Rate Graph Viewer')
fig.canvas.mpl_connect('close_event', handle_close)
ax.set_title(name+"'s Heart Rate Waveform\n"+timestamp)
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
plt.subplots_adjust(bottom=0.25)

x = range(0,len(graphList),1)
y = graphList
l = plt.plot(x,y)
plt.axis([0, 50, 0, 500])

axcolor = 'lightgoldenrodyellow'

axpos = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
spos = Slider(axpos, 'Pos', 0, len(graphList))

def update(val):
    pos = spos.val
    ax.axis([pos,pos+50,0,500])
    fig.canvas.draw_idle()

spos.on_changed(update)

plt.show()
