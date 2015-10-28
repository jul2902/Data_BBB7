#!/usr/bin/python

import mraa as m
import Adafruit_BBIO.ADC as ADC
import time

l = []
x = 0
pwm = m.Pwm(13)
pwm.period_us(16431)
pwm.enable(True)
pwm.write(0.075)
ADC.setup()

while 1:
#	value = ADC.read("P9_40")
#	voltage = value * 1.8
#	print voltage
#	time.sleep(0.1)

#	value1 = ADC.read("P9_40")
#	time.sleep(0.02)
#	value2 = ADC.read("P9_40")
#	voltage = (value2 + value1)*0.9
#	print voltage
#	time.sleep(0.5)
	for x in range(0,100):
		l = []
		l.append(ADC.read("P9_40"))
	
	voltage = (min(l) + max(l))*0.9
	pwm.write(voltage/3.6)
	print voltage	
	
#	l.extend(ADC.read("P9_40")

#	time1 = time.time()
#	value1 = ADC.read("P9_40")	
#	time2 = time.time()
#	value2 = ADC.read("P9_40")
#	time3 = time.time()
#	print time1
#	print time2
#	print time3

	
#	time.sleep(1)
