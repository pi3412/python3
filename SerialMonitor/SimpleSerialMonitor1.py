import serial
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

COM = 'COM3'# /dev/ttyACM0 (Linux)
BAUD = 115200

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
time.sleep(1)
print(ser.name)

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)


def animate(i):
    if (ser.in_waiting>0):
        myData = ser.readline().decode().strip('\r\n')
        print(myData)
        einzelDaten = myData.split(',')
        if(einzelDaten[0] == 'YPR'):
            ax.clear()
            line, = ax.plot([0, -float(einzelDaten[1])/180*np.pi], [0, 1])


ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()
