#!/usr/bin/python
import serial #Import Serial Library
from tkinter import *
from time import sleep

root = Tk()
root.minsize(300,300)
root.geometry("500x500")

var = StringVar()
degreesText = " F"
#arduinoSerialData = serial.Serial('/dev/cu.usbmodemFD121', 9600) #object...tell it which COMPORT are you on?
arduinoSerialData = serial.Serial('/dev/cu.usbmodem641', 9600) #object...tell it which COMPORT are you on?

def update():
	while True:
		line = arduinoSerialData.readline()
		line = line.decode('utf-8')
		var.set(line + degreesText)
		root.update()
		sleep(1)

def set_temperature():
	temp = entry_1.get()
	temp = temp.encode('utf-8')
	arduinoSerialData.write(temp)
	print("Temperature set to", temp)

#Setting the logo
#backgroundPic = PhotoImage(file = "images/mblue.gif")
#root.configure(background = backgroundPic)


#creates the top frame
topFrame = Frame(root)
topFrame.pack()

#creates the bottom frame
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#Setting the logo
logoPic = PhotoImage(file = "images/logo.gif")
logo = Label(topFrame, image=logoPic)
logo.image = logoPic #reference
logo.pack(side=TOP)

#Label that prints the degrees
label = Label(topFrame, textvariable = var)
label.pack(side=BOTTOM)

#create label
label_1 = Label(bottomFrame, text="Set Temperature")
#create entry form
entry_1 = Entry(bottomFrame)
#bind label to the frame
label_1.grid(row=0, column=0)
#bind entry form to the frame
entry_1.grid(row=1, column=0)

button = Button(bottomFrame, text="Enter", fg="red", command=set_temperature)
button.grid(row=2, column=0)

root.after(1,update)
root.mainloop()
