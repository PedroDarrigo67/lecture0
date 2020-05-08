import sqlite3




def getDeveloperInfo(id):
    try:
        sqliteConnection = sqlite3.connect('database.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from principal where id = ?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        
        for row in records:
        #    print("id = ", row[1])
            print("nroticket  = ", row[2])
        #    print("detalle  = ", row[3])
        #    print("fecha  = ", row[4])
        cursor.close()

        print("Printing ID ", id)
        print("detalle ", row[2])

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

getDeveloperInfo(1)