#!/usr/bin/env python

import sys

try:
    import pygtk

    pygtk.require("2.0")
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)


class LexicGUI:
    """This is the PyWine application"""

    def __init__(self):
        # Set the Glade file
        self.gladefile = "LexicGUI.glade"
        self.wTree = gtk.glade.XML(self.gladefile, "mainWindow")

        # Create our dictionay and connect it
        dic = {"on_mainWindow_destroy": gtk.main_quit
            , "testClick": self.TestFunction}
        self.wTree.signal_autoconnect(dic)

    def TestFunction(self, widget):
        """Called when the use wants to add a wine"""

        print "Test Function Was Run"


if __name__ == "__main__":
    test = LexicGUI()
    gtk.main()