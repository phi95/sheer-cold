#!/usr/bin/python
import serial #Import Serial Library
from Tkinter import *
from time import sleep

root = Tk()
root.minsize(300,300)
root.geometry("500x500")

var = StringVar()
degreesText = " F"
arduinoSerialData = serial.Serial('/dev/cu.usbmodemFD121', 9600) #object...tell it which COMPORT are you on?

def update():
	while 1:
		var.set(arduinoSerialData.readline() + degreesText)
		root.update()
		sleep(1)

label = Label(root, textvariable = var)
label.pack()

root.after(1,update)
root.mainloop()
