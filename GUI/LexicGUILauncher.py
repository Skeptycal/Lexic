#!/usr/bin/env python3

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class myWindow (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="LexicGUITest")

        global WindowVar
        WindowVar = self

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        self.prediction1 = Gtk.Button(label = "Prediction #1")
        self.box.pack_start(self.prediction1, True, True, 0)

        self.prediction2 = Gtk.Button(label = "Prediction #2")
        self.box.pack_start(self.prediction2, True, True, 0)

        self.prediction3 = Gtk.Button(label = "Prediction #3")
        self.box.pack_start(self.prediction3, True, True, 0)

        self.prediction4 = Gtk.Button(label = "Prediction #4")
        self.box.pack_start(self.prediction4, True, True, 0)

        self.prediction5 = Gtk.Button(label = "Prediction #5")
        self.box.pack_start(self.prediction5, True, True, 0)

        self.prediction6 = Gtk.Button(label = "Prediction #6")
        self.box.pack_start(self.prediction6, True, True, 0)

        self.prediction7 = Gtk.Button(label = "Prediction #7")
        self.box.pack_start(self.prediction7, True, True, 0)

        self.prediction8 = Gtk.Button(label = "Prediction #8")
        self.box.pack_start(self.prediction8, True, True, 0)

        self.prediction9 = Gtk.Button(label = "Prediction #9")
        self.box.pack_start(self.prediction9, True, True, 0)

def on_prediction_click(widget, sn):
    print "Suggestion #" + sn + " was pressed."
    #Return userchoice to script that emulates keypresses.

win = myWindow()

win.connect("delete-event", Gtk.main_quit)

win.prediction1.connect("clicked", on_prediction_click, "1")
win.prediction2.connect("clicked", on_prediction_click, "2")
win.prediction3.connect("clicked", on_prediction_click, "3")
win.prediction4.connect("clicked", on_prediction_click, "4")
win.prediction5.connect("clicked", on_prediction_click, "5")
win.prediction6.connect("clicked", on_prediction_click, "6")
win.prediction7.connect("clicked", on_prediction_click, "7")
win.prediction8.connect("clicked", on_prediction_click, "8")
win.prediction9.connect("clicked", on_prediction_click, "9")



win.show_all()

Gtk.main()
