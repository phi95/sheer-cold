#!/usr/bin/python
import serial #Import Serial Library
from tkinter import *
import tkinter as tk
from time import sleep
import simpleaudio as sa

root = tk.Tk()
graph = tk.Tk()
graphOn = False
currentTemp = 0
setTemp = 0
checkTemp = False

var = StringVar()
degreesText = " F"
arduinoSerialData = serial.Serial('/dev/cu.usbmodemFD121', 9600) #object...tell it which COMPORT are you on?
#arduinoSerialData = serial.Serial('COM4', 9600) #object...tell it which COMPORT are you on?
#arduinoSerialData = serial.Serial('/dev/cu.usbmodem641', 9600)


#initialize the graph
graph.configure(background="light blue")
graphlabel = Label(graph, text="graph text")
graphlabel.pack()
'''
backgroundPicGraph = PhotoImage(file = "images/graphBlue.gif")
backgroundGraph = Label(root, image = backgroundPicGraph)
'''
#backgroundGraph.image = backgroundPicGraph #reference
#backgroundGraph.pack()


def setCurrentTemp(x):
	currentTemp = x

def getCurrentTemp(): 
	return currentTemp

def update():

	count = 0
	while True:
		line = arduinoSerialData.readline()
		line = line.decode('utf-8')
		global checkTemp
		if checkTemp:
			global currentTemp, setTemp
			if currentTemp < setTemp:
				playAlarm()
				checkTemp = False
		if '&' in line:
			line = str(line)
			line = line.replace("&","")
			line = int(line)
			global set_temp
			set_temp = line
			print("Temperature is now", str(line) + ".")
			root.update()
		else:
			setCurrentTemp(int(float(line)))
			
			#update graph
			count += 1
			update_graph(count)

			#update the temperature display
			line = line.replace('\n', '').replace('\r', '')
			var.set(line + degreesText)
			root.update()
			sleep(1)

def set_temperature():
	setTemp = int(float(entry.get()))
	checkTemp = True
	print("Setting temperature to", setTemp + "...")
	setTemp = setTemp.encode('utf-8')
	arduinoSerialData.write(setTemp)

def playAlarm():
    wave_obj = sa.WaveObject.from_wave_file("beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def update_graph(count):
	graphlabel = Label(graph, text="graph text" + str(count))
	graphlabel.pack()

#background
backgroundPic = PhotoImage(file = "images/mblue.gif")
background = Label(root, image = backgroundPic)
background.image = backgroundPic #reference
background.pack()

#Setting the logo
logoPic = PhotoImage(file = "images/logo.gif")
logo = Label(root, image=logoPic)
logo.image = logoPic #reference
logo.place(x = 0, y = 0)

#Label that prints the degrees
label = Label(root, textvariable = var, fg = 'white', bg = 'black', font = ("Times", 40))
label.place(relx=.5, anchor = CENTER, y = 130)

#Set temp label
setTempText = Label(root, text="Set Temperature: ", fg = 'white', bg = 'black', font = ("Times", 15))
setTempText.place(relx = .28, anchor = CENTER, y = 250)

#create entry form
entry = Entry(root, bg = 'black', fg = 'white', font = ("Times", 15))
entry.place(relx = .6, anchor = CENTER, y = 250)

button = Button(root, text="Enter", command=set_temperature)
button.configure(bg = 'black')
button.place(relx = .5, anchor = CENTER, y = 300)

root.after(1,update)
root.mainloop()
