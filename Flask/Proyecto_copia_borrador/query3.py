import sqlite3
# https://pynative.com/python-sqlite-select-from-table/

def readLimitedRows(rowSize):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from principal"""
        cursor.execute(sqlite_select_query)
        print("Reading ", rowSize, " rows")
        records = cursor.fetchmany(rowSize)
        print("Printing each row \n")
        for row in records:
         #    print("id = ", row[1])
             print("nroticket  = ", row[2])
         #    print("detalle  = ", row[3])
         #    print("fecha  = ", row[4])
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readLimitedRows(2)