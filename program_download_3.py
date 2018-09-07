#THIS PROGRAM RUNS WITHOUT THE COMMAND LISTITOP, I THINK IT IS NOT NECESSARY
import serial
from time import sleep

waitTime = 1
ser = serial.Serial('COM4', 19200, timeout=0,stopbits=2, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port
print(ser.name)          

ser.write(b'1;1;CNTLON\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;9;LOAD=PROJECT.MB4\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;9;LOAD=PROJECT.MB4\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;9;LOAD=PROJECT.MB4\r')
ser.write(b'1;9;EDATA10 MOV P1\r')
ser.write(b'1;9;EDATA20 MOV P2\r')
ser.write(b'1;9;EDATA30 MOV P3\r')
ser.write(b'1;9;EDATA40 END\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;1;CNTLOFF\r')
