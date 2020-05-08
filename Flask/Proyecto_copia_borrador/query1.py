import sqlite3

ind = 3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * FROM principal WHERE id=2"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchone(2) 
        #for row in records:
        #    print("detalle: ", row[2])
         
        cursor.close()

        detal = row[2]
        print(detal)

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()