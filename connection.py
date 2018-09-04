#THIS PART IS NOT NECESSARY
import serial
from time import sleep

waitTime = 1
ser = serial.Serial('COM4', 19200, timeout=0,stopbits=2, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port
print(ser.name)  

ser.write(b'1;1;OPEN=NARCUSR\r')
ser.write(b'1;1;PARRLNG\r')
ser.write(b'1;1;PDIRTOP\r')
ser.write(b'1;1;CNTLON\r')
ser.write(b'1;1;PRGRD\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;1;RSTPRG\r')
ser.write(b'1;1;FDELCOSIROP.MP4\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;1;RSTPRG\r')
ser.write(b'1;1;LOAD=COSIROP.MP4\r')
ser.write(b'1;1;EDATA1\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;1;RSTPRG\r')
ser.write(b'1;1;PRGLOAD=COSIROP.MB4\r')
ser.write(b'1;1;PPOSF\r')
ser.write(b'1;1;CNTLOFF\r')
ser.write(b'1;1;PARMEXTL\r')