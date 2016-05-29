#!/usr/bin/python3

import sys
import os.path
import sqlite3
import mimetypes

#TODO: Add database versions
#TODO: Add something to make sure we don't parse the same text file twice.

con = None
cursor = None

def initiateDB():
    try:
        con = sqlite3.connect('MarkovComplete.db')
        cursor = con.cursor()
        if not cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Completions'").fetchone():
            cursor.execute("CREATE TABLE Completions(PrevWord TEXT, Word TEXT, Weight INT)")
    except sqlite3.Error:
        raise Exception("Could not connect to database")
    finally:
        con.commit()
        con.close()

#TODO: Make this more effecient, as to not recreate the DB connection each time.
def addToDatabase(word1, word2):
    con = sqlite3.connect('MarkovComplete.db')
    cursor = con.cursor()
    if cursor.execute("SELECT * FROM Completions WHERE PrevWord=? AND Word=?", (word1, word2)).fetchone():
        print("Incrementing Weight")
        cursor.execute("UPDATE Completions SET Weight=Weight+1 WHERE PrevWord=? AND Word=?", (word1, word2))
    else:
        print("Creating row")
        cursor.execute("INSERT INTO Completions (PrevWord, Word, Weight) VALUES (?, ?, ?)", (word1, word2, 1))
        print(cursor.lastrowid)
    con.commit()
    con.close()


# From https://stackoverflow.com/questions/17044259/python-how-to-check-if-table-exists
def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False


def parse(file_url):
    initiateDB()
    with open(file_url, 'r') as f:
        for line in f:
            prevWord = ""
            for word in line.split():
                addToDatabase(prevWord, word)
                prevWord = word

if __name__ == '__main__':

    # Try and catch any wrong input in arguments
    for argument in sys.argv[1:]:
        if not os.path.isfile(argument):
            raise Exception("File " + argument + " does not exist")
        if mimetypes.guess_type(argument)[0] != 'text/plain':
            raise Exception("File " + argument + " is not a plain text file")


    for argument in sys.argv[1:]:
        parse(argument)
