import serial #Import Serial Library

arduinoSerialData = serial.Serial('/dev/cu.usbmodem411', 9600) #object...tell it which COMPORT are you on?

while True:
    #read the data off the serial port,
    #unless there is no data...if not then DONT READ
    if (arduinoSerialData.inWaiting() > 0): #only do the commands IF there is data waiting at the serial port object
        myData = arduinoSerialData.readline()
        print(myData.decode('utf-8'))
