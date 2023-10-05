import sqlite3

def conexionDB():
    try:
        con = sqlite3.connect("Clases/BaseDatos.db")
        return con
    
    except sqlite3.Error:
        print(sqlite3.Error)

conexionDB()
