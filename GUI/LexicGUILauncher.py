#!/usr/bin/env python3

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class myWindow (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="LexicGUITest")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.label1 = Gtk.Label("Label1")
        self.box.pack_start(self.label1, True, True, 0)

        self.label2 = Gtk.Label("Label2")
        self.box.pack_start(self.label2, True, True, 0)

win = myWindow()

win.connect("delete-event", Gtk.main_quit)

win.show_all()

Gtk.main()
