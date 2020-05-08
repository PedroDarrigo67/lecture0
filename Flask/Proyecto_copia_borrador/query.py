import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * FROM principal WHERE id=2"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("nroticket: ", row[1]) 
            print("detalle: ", row[2])
            print("fecha: ", row[3])
            print("area_id: ", row[4])
            print("cliente_id:", row[5])
            print("\n")

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