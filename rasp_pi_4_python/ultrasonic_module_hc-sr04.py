import time
import lgpio
from hcsr04 import sensor

PULSE = 13
ECHO = 6

h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, PULSE)
lgpio.gpio_claim_input(h, ECHO)
x = hcsr04sensor.sensor.Measurement

distance_warm = x.basic_distance(trig, echo)

temp = -30
distance_cold = x.basic_distance(trig, echo, celsius=temp)
print("The distance at  20 Celsius is {} cm's".format(distance_warm))
print("The distance at -30 Celsius is {} cm's".format(distance_cold))

def pulse():
	lgpio.tx_pulse(h, PULSE, 15, 0, 0,  1)



try:
	while True:
		pulse()
		
		print(lgpio.gpio_read(h, ECHO))
		time.sleep(1)
except KeyboardInterrupt:
	lgpio.gpiochip_close(h)