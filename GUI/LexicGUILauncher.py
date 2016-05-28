#!/usr/bin/env python3

#Import dependencies
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

#Customizable variables

#The amount of buttons that will be created:
buttonAmount = 9

#Create class for the main window
class mainWindow (Gtk.Window):
    #Initiating function for the window
    def __init__(self):
        Gtk.Window.__init__(self, title="LexicGUITest")

        #Create vertical box that the buttons will be placed in
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        #Add the box to the window
        self.add(self.box)

win = mainWindow()

#Function for creating the buttons
def createButtons(amount):
    i = 1
    while i <= amount :
        #Add the buttons to the window class
        setattr(win, "prediction" + str(i), Gtk.Button(label = "Prediction #" + str(i)))
        #Add the buttons to the box
        win.box.pack_start(getattr(win, "prediction" + str(i)), True, True, 0)
        #Connect the buttons clicked event to the on_prediction_click function
        getattr(win, "prediction" + str(i)).connect("clicked", on_prediction_click, i)
        i += 1

def on_prediction_click(widget, sn):
    print "Suggestion #" + str(sn) + " was pressed."
    #Return userchoice to script that emulates keypresses.

#Connect the closing of the main window, to ending the script with Gtk.main_quit
win.connect("delete-event", Gtk.main_quit)

#Run the createButtons function
createButtons(buttonAmount)

#Show the window and it's children(buttons)
win.show_all()

#Executes the main function of Gtk
Gtk.main()
