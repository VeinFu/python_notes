#!/usr/bin/env python
# *-* coding: utf-8 *-*

from Tkinter import *
import os,sys
import tkMessageBox

class Application(Frame):
		def __init__(self, master=None):
				Frame.__init__(self, master)
				self.pack()
				self.createWidgets()

		def get_cpu_info(self):
				message = os.popen("dmidecode -t processor").read().split()
				tkMessageBox.showinfo("CPU Info", message)

		def createWidgets(self):
				self.helloLabel = Label(self, text='CPU Info')
				self.helloLabel.pack()
				self.quitButton = Button(self, text='DISPLAY', command=self.get_cpu_info)
				self.quitButton.pack()

app = Application()
app.master.title("Hello World")
app.mainloop()
