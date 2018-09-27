import serial

ser = serial.Serial('COM4', 19200, timeout=0,stopbits=2, parity=serial.PARITY_EVEN, rtscts=1)  # open serial port
print(ser.name) 

def writeFunction(cmd):
    """This function is responsible for sending the serial command"""
    command = ('1;9;EDATA%s\r' % (cmd))
    command_to_byte = str.encode(command) #converts the string built in bytes to be transmitted in serial
    ser.write(command_to_byte)

def definePosition(PosName, coords, overrideFlag, structureFlag):
    """This function writes the position to be saved, it can save the position with the structure flags or
    without it"""
    if overrideFlag:
        posBuffer = '%s=(%.2f,%.2f,%.2f,%.2f,%.2f,%.2f)' %(PosName, coords[0], coords[1], coords[2], coords[3], 
        coords[4], coords[5])
        
    else:
        posBuffer = '%s=(%.2f,%.2f,%.2f,%.2f,%.2f,%.2f)(%d,%d)' %(PosName, coords[0], coords[1], coords[2], coords[3], 
        coords[4], coords[5], structureFlag[0], structureFlag[1])
        
    writeFunction(posBuffer)
        

def positionNoFlag(PosName, coords):
    """This function writes the postion with no flags, on the format P1=(X,Y,Z,A,B,C)"""
    definePosition(PosName, coords, True, [0,0])

def positionFlag(posName, coords, structureFlag):
    """This function writes the position with the flag, on the Format P1=(X,Y,Z,A,B,C)(L1,L2)"""
    definePosition(posName, coords, False, structureFlag)

#Write the positions here
def main():
    positionNoFlag('P2', [210.19,250.50,550.00,0.00,90.00,0.00])
    positionNoFlag('P3', [67.79,31.61,854.70,28.49,20.00,0.00])
    positionNoFlag('P1', [404.71,188.72,186.91,-15.48,145.00,0.00] )
    positionNoFlag('J1', [60.00, 0.00, 60.00, 0.00, 0.00, 0.00])
    positionNoFlag('J2', [60.00, 0.00, 110.00, 0.00, 0.00, 0.00])

#sending to the controller
ser.write(b'1;1;CNTLON\r') #TURNS THE CONTROLLER ON
ser.write(b'1;1;SAVE\r') #INDICATES THE SAVING OF A NEW ITEM
ser.write(b'1;9;LOAD=VICTOR.MB4\r') #CREATES THE PROJECT NAME
main()
ser.write(b'1;1;SAVE\r')#FINSIH SAVING
ser.write(b'1;1;CNTLOFF\r')#TURNS THE CONTROLLER OFF