printLineNum=0

def writeFunction(cmd, lineNum):
    """This function is responsible for sending the serial command"""
    global printLineNum
    printLineNum = lineNum
    printLineNum += 10
    words=("1;9;EDATA%d %s" % (printLineNum, cmd))
    print(words)

#functions that control the robot movement
#MOV
def MOV_int(lineNum, pos):
    MOVBuffer = 'MOV %s' % (pos)
    writeFunction(MOVBuffer, lineNum)

def MOV(pos):
    MOV_int(printLineNum, pos)

#MVS
def MVS_int(lineNum, pos):
    MVSBuffer = 'MVS %s' % (pos)
    writeFunction(MVSBuffer, lineNum)

def MVS(pos):
    MVS_int(printLineNum, pos)

#MVR
def MVR_int(lineNum, pos1, pos2, pos3):
    MVRBuffer= 'MVR %s, %s, %s' %(pos1, pos2, pos3)
    writeFunction(MVRBuffer, lineNum)

def MVR(pos1, pos2, pos3):
    MVR_int(printLineNum, pos1, pos2, pos3)

#MVR2
def MVR2_int(lineNum, pos1, pos2, pos3):
    MVR2Buffer= 'MVR2 %s, %s, %s' %(pos1, pos2, pos3)
    writeFunction(MVR2Buffer, lineNum)

def MVR2(pos1, pos2, pos3):
    MVR2_int(printLineNum, pos1, pos2, pos3)

#MVR3
def MVR3_int(lineNum, pos1, pos2, pos3):
    MVR3Buffer= 'MVR3 %s, %s, %s' %(pos1, pos2, pos3)
    writeFunction(MVR3Buffer, lineNum)

def MVR3(pos1, pos2, pos3):
    MVR3_int(printLineNum, pos1, pos2, pos3)

def END_int(lineNum):
    ENDBuffer = 'END'
    writeFunction(ENDBuffer, lineNum)

def END():
    END_int(printLineNum)

MOV('P1')
END()






