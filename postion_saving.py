import serial
from time import sleep

waitTime = 1
ser = serial.Serial('COM4', 19200, timeout=0,stopbits=2, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port
print(ser.name)          

ser.write(b'1;1;CNTLON\r') #TUNRS THE CONTROLLER ON
ser.write(b'1;1;SAVE\r') #INDICATES THE SAVING OF A NEW ITEM
ser.write(b'1;9;LOAD=PROJECT.MB4\r') #CREATES THE PROJECT NAME
ser.write(b'1;9;EDATAP1=(67.79,31.61,854.70,28.49,20.00,0.00)\r') #SAVES THE POSITION Pn WORKSPACE 
ser.write(b'1;9;EDATAP2=(404.71,188.72,186.91,-15.48,145.00,0.00)\r')
ser.write(b'1;9;EDATAP3=(210.19,250.50,550.00,0.00,90.00,0.00)\r')
ser.write(b'1;9;EDATAJ1=(0.00, 0.00, 90.00, 0.00, 0.00, 0.00)\r')#SAVES THE POSITION IN Jn JOINT SPACE
ser.write(b'1;1;SAVE\r')#FINSIH SAVING
ser.write(b'1;1;CNTLOFF\r')#TURNS THE CONTROLLER OFF
