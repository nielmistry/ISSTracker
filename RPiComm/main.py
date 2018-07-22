import RPi.GPIO as GPIO
import time
import binascii

OUTPUT_PIN = 17
CLK_PIN = 4
DELAY_TIME = 0.0005

def cycleClock():
	GPIO.output(CLK_PIN, GPIO.HIGH)
	time.sleep(DELAY_TIME)
	GPIO.output(CLK_PIN, GPIO.LOW)
	time.sleep(DELAY_TIME)

def preamble():
	GPIO.output(OUTPUT_PIN, GPIO.HIGH)

	for i in range(0, 7):
		cycleClock()

# Send a string in it's ASCII format over the data wire
def sendWord(word):
	for i in range(0, len(word)):
		character = word[i]
		byte = int(binascii.hexlify(character),16)
		# Go through every bit of the byte
		for j in range(0, 8):

			# Get the Most Significant Bit
			bit = byte & 2**7
			bit >>= 7 

			# Shift the byte by one bit (i.e. 10101010 becomes 01010100 (0 padded in at the end))
			byte <<= 1
			byte &= 0xFF

			if bit == 1:
				GPIO.output(OUTPUT_PIN, GPIO.HIGH)
			else:
				GPIO.output(OUTPUT_PIN, GPIO.LOW)
			
			cycleClock()

def infBlink():
	while True:
		GPIO.output(OUTPUT_PIN,GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(OUTPUT_PIN,GPIO.LOW)
		time.sleep(0.5)

# Set the mode of the GPIO module to Broadcom, and setup the pins by setting them to output and bringing them low
GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPUT_PIN, GPIO.OUT)
GPIO.setup(CLK_PIN, GPIO.OUT)
GPIO.output(OUTPUT_PIN, GPIO.LOW)
GPIO.output(CLK_PIN,GPIO.LOW)

toSend = "Hello, world!"
sendWord(toSend)

GPIO.output(OUTPUT_PIN, GPIO.LOW)
GPIO.output(CLK_PIN, GPIO.LOW)

