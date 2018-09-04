import serial
from time import sleep

waitTime = 1
ser = serial.Serial('COM4', 19200, timeout=0,stopbits=2, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port
print(ser.name)          

ser.write(b'1;1;CNTLON\r')
ser.write(b'1;1;FCHECKPROJECT.MB4\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;1;SLOTINIT\r')
ser.write(b'1;1;RSTPRG\r')
ser.write(b'1;1;PRGLOAD=PROJECT.MB4\r')
ser.write(b'1;1;SRVON\r')
ser.write(b'1;1;STATE\r')
ser.write(b'1;1;RUN\r')
ser.write(b'1;1;CNTLOFF\r')
#ser.write(b'1;0;STOP\r')