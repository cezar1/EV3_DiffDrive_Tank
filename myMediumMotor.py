#!/usr/bin/python
from ev3dev.auto import *
from time import sleep
ir = InfraredSensor(); assert ir.connected
ir.mode = 'IR-PROX'
myD=MediumMotor(OUTPUT_D)
assert myD.connected
while ir.value()>30:
	myD.run_forever(duty_cycle_sp=-30)
myD.stop(stop_command='brake')
print myD.position
myD.reset()
#while 1:
#	print myD.position
#	sleep(1)
myD.position_sp=240
myD.duty_cycle_sp=50	
myD.run_to_abs_pos()
#sleep(20)
myTravel2=400
while 1:
	if myD.position>myTravel2-10:
		myD.position_sp=30
		myD.run_to_abs_pos()
	if myD.position<40:
		myD.position_sp=myTravel2
		myD.run_to_abs_pos()
	print str(myD.position) + " " + str(ir.value())
	#sleep(0.1)
