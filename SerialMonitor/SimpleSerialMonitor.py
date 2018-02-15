import serial
from time import sleep
import sys


COM = 'COM3'# /dev/ttyACM0 (Linux)
BAUD = 115200

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(1)
print(ser.name)

while True:
	#val = str(ser.readline().decode().strip('\r\n'))#Capture serial output as a decoded string
	#print(val, end="\r", flush=True)
    if (ser.in_waiting>0):
        myData = ser.readline().decode().strip('\r\n')
        print(myData)