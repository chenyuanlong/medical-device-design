#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import pylab
import pexpect
import time
from pylab import *
#from hrm_demo import getHR

xAchse=pylab.arange(0,100,1)
yAchse=pylab.array([0]*100)

fig = pylab.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("Realtime Heart Rate Waveform")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.axis([0,100,-1.5,1.5])
line1=ax.plot(xAchse,yAchse,'-')

manager = pylab.get_current_fig_manager()

values=[]
values = [0 for x in range(100)]

Ta=0.01
fa=1.0/Ta
fcos=3.5

constant=cos(2*pi*fcos*Ta)
T0=1.0
T1=constant

#pexpect code
addr = "D3:E0:D2:08:2B:8F"
try:
 gt = pexpect.spawn("gatttool -b " + addr + " -t random --interactive")
 gt.expect(r"\[LE\]>")
 gt.sendline("connect")
 gt.expect(r"\[LE\]>")
 i = gt.expect(["Connection successful.", r"\[CON\]"], timeout=30)
 gt.expect(r"\[LE\]>", timeout=30)
except pexpect.TIMEOUT:
 print("Connection timeout.")
except KeyboardInterrupt:
 print("Received keyboard interrupt. Quitting cleanly.")
#pexpect code

def SinwaveformGenerator(arg):
  global values,T1,constant,T0,i
  #ohmegaCos=arccos(T1)/Ta
  #print("fcos=", ohmegaCos/(2*pi), "Hz")
  
  #hr acquisition code
  gt.sendline("char-read-hnd 0x0029")
  gt.expect(r"Characteristic value/descriptor: .*", timeout=10)
  hr = gt.after.decode().split('\n', 1)[0].split(' ', 1)[1].split(' ', 1)[1].split(' ', 1)[1]
  hr =  int("0x"+hr,16)
  print("The heart rate is: "+str(hr))
  Tnext = hr
  #hr acquisition code
  #Tnext=((constant*T1)*2)-T0
  values.append(Tnext)
  T0=T1
  T1=Tnext
  time.sleep(0.25)

def RealtimePloter(arg):
  global values
  CurrentXAxis=pylab.arange(len(values)-100,len(values),1)
  line1[0].set_data(CurrentXAxis,pylab.array(values[-100:]))
  ax.axis([CurrentXAxis.min(),CurrentXAxis.max(),50,100])
  manager.canvas.draw()
  #manager.show()

timer = fig.canvas.new_timer(interval=20)
timer.add_callback(RealtimePloter, ())
timer2 = fig.canvas.new_timer(interval=20)
timer2.add_callback(SinwaveformGenerator, ())
timer.start()
timer2.start()

pylab.show()
