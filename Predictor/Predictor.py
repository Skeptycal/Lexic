#!/usr/bin/python3

import sqlite3
import sys
from time import sleep, time
import ctypes as ct
from ctypes.util import find_library

con = None
cursor = None



#Crash if not on linux
assert("linux" in sys.platform)

def initiateDB(fileName):
    #Try and connect to SQL, crash if that doesn't work
    try:
        con = sqlite3.connect(fileName)
    except sqlite3.Error:
        raise Exception("Could not connect to database")

#Creates a connection object, with our first argument which is the filename of the DB file. Then we create a cursor object, which is for navigating the DB, and use it to get the list of words corresponding to PrevWord
def getWords(PrevWord):
    con = sqlite3.connect(sys.argv[1])
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Completions WHERE PrevWord=? ORDER BY Weight DESC", (PrevWord,))
    return cursor



def cliLoop():
    #Hold on to your butts
    while True:
        #While true, we ask the user for input, and then show them what's in getWords()
        textInput = input("Enter previous word: ")
        words = getWords(textInput)
        for i in range(10):
            row = words.fetchone()

            if row == None:
                break

            print(row[1])

#If this is not a library, but instead just executed on it's own, we'll do these things.
if __name__ == '__main__':

    initiateDB(sys.argv[1])
    if len(sys.argv) < 2:
        raise Exception("Need first argument for database")
    initiateDB(sys.argv[1])
    cliLoop()
