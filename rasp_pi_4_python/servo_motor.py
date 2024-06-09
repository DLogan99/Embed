import time
import lgpio

SERVO = 13

h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, SERVO)
servo_pos = 5.4

def change_stepper():
	global servo_pos
	servo_pos += 1
	print(servo_pos)


try:
	while True:
		lgpio.tx_pwm(h, SERVO, 50, servo_pos, 0, 0)
		# change_stepper()
		time.sleep(1)
except KeyboardInterrupt:
	lgpio.gpio_write(h, SERVO, 0)
	lgpio.gpiochip_close(h)