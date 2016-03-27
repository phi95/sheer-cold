#!/usr/bin/python
import serial #Import Serial Library
from tkinter import *
import tkinter as tk
from time import sleep
import simpleaudio as sa


root = tk.Tk()
graphOn = False
currentTemp = 0
setTemp = 0
checkTemp = False
loop = True

var = StringVar()
degreesText = " F"
#arduinoSerialData = serial.Serial('/dev/cu.usbmodemFD121', 9600) #object...tell it which COMPORT are you on?
#arduinoSerialData = serial.Serial('COM4', 9600) #object...tell it which COMPORT are you on?
arduinoSerialData = serial.Serial('/dev/cu.usbmodem641', 9600)


#initialize the graph

'''
backgroundPicGraph = PhotoImage(file = "images/graphBlue.gif")
backgroundGraph = Label(root, image = backgroundPicGraph)
'''
#backgroundGraph.image = backgroundPicGraph #reference
#backgroundGraph.pack()


def setCurrentTemp(x):
	global currentTemp
	currentTemp = x

def getCurrentTemp():
	global currentTemp
	return currentTemp

def setSetTemp(x):
	global setTemp
	setTemp = x

def getSetTemp():
	global setTemp
	return setTemp

def update():

	count = 0
	time_count = 0

	graph_file_buffer = [None]*3		#initialize the output buffer
	graph_file_buffer[1] = ','			#place comma for formatting

	while loop:


		graph_file_buffer[0] = str(time_count)
		time_count += 1							#keep track of the time to write to a file for graphing

		line = arduinoSerialData.readline()
		line = line.decode('utf-8')
		global checkTemp
		if checkTemp:
			if getCurrentTemp() < getSetTemp():
				playAlarm()
				checkTemp = False

		if '&' in line:
			line = str(line)
			line = line.replace("&","")
			line = int(line)
			print("Temperature is now", str(line) + ".")
			root.update()

		else:
			#update graph
			count += 1

			#update the temperature display
			line = line.replace('\n', '').replace('\r', '')
			setCurrentTemp(float(line))
			var.set(line + degreesText)

			graph_file_buffer[2] = str(line)	#initialize buffer
			write_to_file(graph_file_buffer)	#write the the output to a text file for graphing
			clear_buffer(graph_file_buffer)		#clear the buffer

			root.update()
			sleep(1)

def write_to_file(graph_file_buffer):
	target = open('plot.txt', 'a')

	output = ""
	for i in graph_file_buffer:
		output += i

	target.write(output+'\n')
	target.close()



def clear_buffer(graph_file_buffer):
	graph_file_buffer[0] = ""
	graph_file_buffer[2] = ""

def set_temperature():
	global checkTemp
	setTemp = entry.get()
	checkTemp = True
	print("Setting temperature to", setTemp , "...")
	setTemp = setTemp.encode('utf-8')
	arduinoSerialData.write(setTemp)
	setSetTemp(float(setTemp))

def playAlarm():
    wave_obj = sa.WaveObject.from_wave_file("beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def quit():
	global loop
	loop = False
	sys.exit(0)



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

button2 = Button(root, text=" Quit  ", command=quit)
button2.configure(bg = 'black')
button2.place(relx = .70, anchor = CENTER, y = 300)


root.after(1,update)
root.mainloop()
