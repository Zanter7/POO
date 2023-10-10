import sqlite3

def conexionDB():
    try:
        con = sqlite3.connect("Proyecto/BaseDatosClientes.db")
        return con
    
    except sqlite3.Error:
        print(sqlite3.Error)

def CreaTablaProductos(DB):
    
    cursor = DB.cursor()
    cursor.execute("CREATE TABLE productos(id integer PRIMARY KEY autoincrement, NombreProducto text, Peso real, FechaVencimineto date, PrecioCompra real, PrecioVenta real)")
    DB.commit()

def CreaTablaClientes(DB):
    
    cursor = DB.cursor()
    cursor.execute("CREATE TABLE Clientes(Identificacion integer, NombreCliente text, ApellidoCliente text, DireccionCliente text, TelefonoCliente integer, CorreoCLiente text)")
    DB.commit()