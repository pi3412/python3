import serial
import time
import sys

COM = 'COM3'# /dev/ttyACM0 (Linux)
BAUD = 115200
DATAPOINTS = 10
FILEPARTS = 50

ser = serial.Serial(COM, BAUD, timeout = .1)

path = 'C:/data/Magneto1.txt'

print('Waiting for device');
time.sleep(1)
print(ser.name)

for CounterFP in range(FILEPARTS):
    Counter = 0
    open_file = open(path,'a')
    while (Counter < DATAPOINTS):
        if (ser.in_waiting>0):
            myData = ser.readline().decode().strip('\r\n')
            einzelDaten = myData.split(',')
            if(einzelDaten[0] == 'RawMag'):
                open_file.write(einzelDaten[1])
                open_file.write(' ')
                open_file.write(einzelDaten[2])
                open_file.write(' ')
                open_file.write(einzelDaten[3])
                open_file.write('\n')
                print(Counter)
                Counter = Counter + 1
    open_file.close()
