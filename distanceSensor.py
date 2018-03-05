import serial

arduinoSerialData = serial.Serial('/dev/ttyUSB0', 9600)

while (1==1):
    if (arduinoSerialData.inWaiting() > 0):
        myData = arduinoSerialData.readline()
        distance = float(myData)
        if distance > 9:
            arduinoSerialData.write('1')
        elif distance < 9:
            arduinoSerialData.write('2')
        #print(distance)
       
