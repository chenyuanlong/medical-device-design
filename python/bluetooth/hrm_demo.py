#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pexpect
import time

#gatttool -i hci0 -b D3:E0:D2:08:2B:8F -t random --interactive
#char-read-hnd 0x0029

addr = "D3:E0:D2:08:2B:8F"


try:
 gt = pexpect.spawn("gatttool -b " + addr + " -t random --interactive")
 gt.expect(r"\[LE\]>")
 gt.sendline("connect")
 gt.expect(r"\[LE\]>")
 i = gt.expect(["Connection successful.", r"\[CON\]"], timeout=30)
 gt.expect(r"\[LE\]>", timeout=30)
 
 while 1:
  gt.sendline("char-read-hnd 0x0029")
  gt.expect(r"Characteristic value/descriptor: .*", timeout=10)
  hr = gt.after.split('\n', 1)[0].split(' ', 1)[1].split(' ', 1)[1].split(' ', 1)[1]
  hr =  int("0x"+hr,16)
  print("The heart rate is: "+str(hr))
  time.sleep(1)
except pexpect.TIMEOUT:
  print("Connection timeout.")
except KeyboardInterrupt:
  print("Received keyboard interrupt. Quitting cleanly.")
