import RPi.GPIO as GPIO
import time
import binascii

OUTPUT_PIN = 17
CLK_PIN = 4
DELAY_TIME = 0.0005
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
				GPIO.output(OUTPUT_PIN, GPIO.HIGH)
			else:
				GPIO.output(OUTPUT_PIN, GPIO.LOW)
			GPIO.output(CLK_PIN, GPIO.HIGH)
			time.sleep(DELAY_TIME)
			GPIO.output(CLK_PIN, GPIO.LOW)
			time.sleep(DELAY_TIME)

def infBlink():
	while True:
		GPIO.output(OUTPUT_PIN,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(OUTPUT_PIN,GPIO.LOW)
		time.sleep(0.5)


GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPUT_PIN, GPIO.OUT)
GPIO.setup(CLK_PIN, GPIO.OUT)
GPIO.output(OUTPUT_PIN, GPIO.LOW)
GPIO.output(CLK_PIN,GPIO.LOW)

toSend = "Hello, world!"
sendWord(toSend)



