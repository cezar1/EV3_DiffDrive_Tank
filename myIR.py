#!/usr/bin/python
from time import sleep
from ev3dev.auto import *
ir = InfraredSensor(); assert ir.connected
ir.mode = 'IR-PROX'
while 1:
	print ir.value()
	sleep(1)
