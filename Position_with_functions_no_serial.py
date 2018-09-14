def writeFunction(cmd):
    """This function is responsible for sending the serial command"""
    words=("1;9;EDATA%s" % (cmd))
    print(words)

def definePosition(PosName, coords, overrideFlag, structureFlag):
    if overrideFlag:
        posBuffer = '%s=(%.2f,%.2f,%.2f,%.2f,%.2f,%.2f)' %(PosName, coords[0], coords[1], coords[2], coords[3], 
        coords[4], coords[5])
        #writeFunction(PosBuffer)
    else:
        posBuffer = '%s=(%.2f,%.2f,%.2f,%.2f,%.2f,%.2f)(%d,%d)' %(PosName, coords[0], coords[1], coords[2], coords[3], 
        coords[4], coords[5], structureFlag[0], structureFlag[1])
        #writeFunction(PosBuffer)
    writeFunction(posBuffer)
        
   

def positionNoFlag(PosName, coords):
    definePosition(PosName, coords, True, [0,0])

def positionFlag(posName, coords, structureFlag):
    definePosition(posName, coords, False, structureFlag)


positionNoFlag('P1', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
positionFlag('P2', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [6,0])


    