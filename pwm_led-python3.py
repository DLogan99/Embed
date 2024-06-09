import time
import lgpio

LED = 13

h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, LED)
led_brightness = 0


try:
	while True:
		led_brightness+=1
		lgpio.tx_pwm(h, LED, 50, led_brightness, 0, 0)
		if led_brightness >= 55:
			led_brightness = 0
		time.sleep(.01)
except KeyboardInterrupt:
	lgpio.gpio_write(h, LED, 0)
	lgpio.gpiochip_close(h)