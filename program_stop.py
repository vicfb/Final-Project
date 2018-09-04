import serial
from time import sleep

waitTime = 2
ser = serial.Serial('COM4', 19200, timeout=0,stopbits=2, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port

ser.write(b'1;0;STOP\r')
 
ser.close()