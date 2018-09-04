import serial
from time import sleep

waitTime = 1
ser = serial.Serial('COM4', 19200, timeout=0,stopbits=2, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port
print(ser.name)          



#Position Saving

ser.write(b'1;1;CNTLON\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;9;LOAD=PROJECT.MB4\r')
ser.write(b'1;9;EDATAP1=(67.79,31.61,854.70,28.49,20.00,0.00)(4,0)\r')
ser.write(b'1;9;EDATAP2=(404.71,188.72,186.91,-15.48,145.00,0.00)(6,0)\r')
ser.write(b'1;9;EDATAJ1=(0.00,90.00,0.00,0.00,0.00,0.00)\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;1;CNTLOFF\r')

#Program download

ser.write(b'1;1;CNTLON\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;9;LOAD=PROJECT.MB4\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;9;LOAD=PROJECT.MB4\r')
ser.write(b'1;9;LISTITOP\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;9;LOAD=PROJECT.MB4\r')
ser.write(b'1;9;EDATA10 OVRD 20\r')
ser.write(b'1;9;EDATA15 MOV P1\r')
ser.write(b'1;9;EDATA20 MOV P2\r')
ser.write(b'1;9;EDATA30 MOV J1\r')
ser.write(b'1;9;EDATA40 END\r')
ser.write(b'1;1;SAVE\r')
ser.write(b'1;1;CNTLOFF\r')

#Start of the program

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