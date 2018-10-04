import serial
from time import sleep
#Write the program name here
ProgName = ''

ser = serial.Serial('COM4', 19200, timeout=0,stopbits=2, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port
print(ser.name)          

ser.write(b'1;1;CNTLON\r')
ser.write(b'1;1;FCHECK%s.MB4\r' % ProgName)
ser.write(b'1;1;SAVE\r')
ser.write(b'1;1;SLOTINIT\r')
ser.write(b'1;1;RSTPRG\r')
ser.write(b'1;1;PRGLOAD=%s.MB4\r' % ProgName)
ser.write(b'1;1;SRVON\r')
ser.write(b'1;1;STATE\r')
ser.write(b'1;1;RUN\r')
ser.write(b'1;1;CNTLOFF\r')
#ser.write(b'1;0;STOP\r')