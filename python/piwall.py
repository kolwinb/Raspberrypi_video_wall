#!/usr/bin/env python

import controler as con

import Tkinter
from Tkinter import *
from tkFileDialog import askopenfilename

root = Tkinter.Tk()

def open():
	openfile();

def reboot():
	con.reboot();

def switchoff():
	con.switchoff();

button = Tkinter.Button(root, text ="Open", command = open)
#button.pack(pady=20, padx=20)
button.grid(row=0,column=0,pady=10,padx=10,ipadx=10)
button = Tkinter.Button(root, text ="reboot", command = reboot)
#button.pack(pady=20, padx=20)
button.grid(row=2,column=0, pady=10,padx=10,ipadx=10)
button=Tkinter.Button(root,text="shutdown", command=switchoff)
button.grid(row=4,column=0)

def openfile():
	name = askopenfilename(initialdir="/home/pi/Videos",
				filetypes=(("mp4","*.mp4"),("All files","*.*")),

				title = "choose a file."
				)
	con.udpstream(name);
	#try:
	#	with open(name,'r') as UseFile:
	#		#print(UseFile.read())
	#		con.udpstream(UseFile);
	#except:
	#	print ("No file exists")

title=root.title("File Opener")
root.mainloop()
