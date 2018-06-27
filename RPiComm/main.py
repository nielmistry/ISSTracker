import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(04, GPIO.OUT)

while True:
	GPIO.output(04,GPIO.HIGH);
	time.sleep(0.5)
	GPIO.output(04,GPIO.LOW);
	time.sleep(0.5)
