import serial
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


COM = 'COM3'# /dev/ttyACM0 (Linux)
BAUD = 115200
DATAPOINTS = 50

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ser = serial.Serial(COM, BAUD, timeout = .1)

RawMag = np.empty(shape=(3,DATAPOINTS))
CalMag = np.empty(shape=(3,DATAPOINTS))

RawMagCounter = 0
CalMagCounter = 0

print('Waiting for device');
time.sleep(1)
print(ser.name)

while ((CalMagCounter < DATAPOINTS) & (RawMagCounter < DATAPOINTS)):
    if (ser.in_waiting>0):
        myData = ser.readline().decode().strip('\r\n')
        print(RawMagCounter, CalMagCounter)
        einzelDaten = myData.split(',')
        print(einzelDaten)
        if(einzelDaten[0] == 'RawMag'):
            RawMag[0,RawMagCounter] = float(einzelDaten[1])
            RawMag[1,RawMagCounter] = float(einzelDaten[2])
            RawMag[2,RawMagCounter] = float(einzelDaten[3])
            ax.scatter(float(einzelDaten[1]), float(einzelDaten[2]), float(einzelDaten[3]), c='r')
            RawMagCounter = RawMagCounter + 1
        if(einzelDaten[0] == 'CalMag'):
            CalMag[0,CalMagCounter] = float(einzelDaten[1])
            CalMag[1,CalMagCounter] = float(einzelDaten[2])
            CalMag[2,CalMagCounter] = float(einzelDaten[3])
            ax.scatter(float(einzelDaten[1]), float(einzelDaten[2]), float(einzelDaten[3]), c='b')
            CalMagCounter = CalMagCounter + 1

print('RawMag:')
print(RawMag)
print('CalMag:')
print(CalMag)


# ax.scatter(xs, ys, zs, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
