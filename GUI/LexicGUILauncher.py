#!/usr/bin/env python3

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

#Customizable variables
buttonAmount = 9

class mainWindow (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="LexicGUITest")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

win = mainWindow()

def createButtons():
    i = 1
    while i <= buttonAmount :
        setattr(win, "prediction" + str(i), Gtk.Button(label = "Prediction #" + str(i)))
        win.box.pack_start(getattr(win, "prediction" + str(i)), True, True, 0)
        getattr(win, "prediction" + str(i)).connect("clicked", on_prediction_click, i)
        i += 1

def on_prediction_click(widget, sn):
    print "Suggestion #" + str(sn) + " was pressed."
    #Return userchoice to script that emulates keypresses.

win.connect("delete-event", Gtk.main_quit)

createButtons()

win.show_all()

Gtk.main()
