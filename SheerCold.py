#!/usr/bin/python
import serial #Import Serial Library
from Tkinter import *
from time import sleep

root = Tk()
root.minsize(300,300)
root.geometry("500x500")
root.title("Sheer Cold")

var = StringVar()
degreesText = " F"
arduinoSerialData = serial.Serial('/dev/cu.usbmodemFD121', 9600) #object...tell it which COMPORT are you on?

def update():
	while 1:
		var.set(arduinoSerialData.readline() + degreesText)
		root.update()
		sleep(1)


#Setting the logo
logoPic = PhotoImage(file = "images/logo.gif")
logo = Label(root, image=logoPic)
logo.image = logoPic #reference
logo.pack()

#Label that prints the degrees
label = Label(root, textvariable = var)
label.pack()

root.after(1,update)
root.mainloop()
