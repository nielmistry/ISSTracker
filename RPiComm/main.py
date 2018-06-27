import RPi.GPIO as GPIO
import time
import binascii

def sendWord(word):
asciiDecode = int(binascii.hexlify(word), 16)
	for i in range(0,asciiDecode.bit_length):
		bit = asciiDecode & 0b01
		asciiDecode = asciiDecode >> 1
		if asciiDecode == 1:
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



