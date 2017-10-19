#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import pylab
import pexpect
import time
import subprocess
from pylab import *
#from hrm_demo import getHR
x=0
xAchse=pylab.arange(0,50,1)
yAchse=pylab.array([0]*50)

fig = pylab.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("Realtime Heart Rate Waveform")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.axis([0,50,0,200])
line1=ax.plot(xAchse,yAchse,'-')

manager = pylab.get_current_fig_manager()

values = [0 for x in range(50)]

cmd = 'gatttool -b D3:E0:D2:08:2B:8F -t random --char-write-req -a 0x2a -n 0100 --listen'
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def getData(arg):
    global p
    line = p.stdout.readline().decode("utf-8")
    if('Characteristic' in line):
        output = ''
    else:
        line = p.stdout.readline().decode("utf-8").split(' ')
        output = line[5]+line[6]
        output =  int("0x"+output,16)
        values.append(output)
        print("The amplitude is: "+str(output))

def RealtimePloter(arg):
  global values
  CurrentXAxis=pylab.arange(len(values)-50,len(values),1)
  line1[0].set_data(CurrentXAxis,pylab.array(values[-50:]))
  ax.axis([CurrentXAxis.min(),CurrentXAxis.max(),0,200])
  manager.canvas.draw()
  #manager.show()

timer = fig.canvas.new_timer(interval=20)
timer.add_callback(RealtimePloter, ())
timer2 = fig.canvas.new_timer(interval=20)
timer2.add_callback(getData, ())
timer.start()
timer2.start()

pylab.show()
