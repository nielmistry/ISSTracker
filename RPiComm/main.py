import RPi.GPIO as GPIO
import time
import binascii

def sendWord(word):
	for i in range(0, len(word)):
		character = word[i]
		byte = int(binascii.hexlify(character),16)
		for j in range(7, -1, -1):
			bit = byte & 2**7
			bit >>= 7 
			byte <<= 1
			byte &= 0xFF

			if bit == 1:
				GPIO.output(4, GPIO.HIGH)
			else:
				GPIO.output(4, GPIO.LOW)
			time.sleep(1)

def infBlink():
	while True:
		GPIO.output(4,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(4,GPIO.LOW)
		time.sleep(0.5)

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

toSend = "Hello, world!"
sendWord(toSend)



