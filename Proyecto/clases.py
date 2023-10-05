import sqlite3


class BaseDeDatos:
    def __init__(self, db_name="Proyecto/BaseDatosClientes.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def guardar(self):
        self.conn.commit()

    def CerrarConexion(self):
        self.conn.close()


class cliente:
    def __init__(self, identificacion, NombreCliente, ApellidoCliente, DireccionCliente, TelefonoCliente, CorreoCliente):

        self.identificacion = identificacion
        self.NombreCliente = NombreCliente
        self.ApellidoCliente = ApellidoCliente
        self.DireccionCliente = DireccionCliente
        self.TelefonoCliente = TelefonoCliente
        self.CorreoCliente = CorreoCliente

    def CrearCliente(self, DB):

        DB.cursor.execute('''
            INSERT INTO clientes (Identificacion,NombreCliente,ApellidoCliente,DireccionCliente,TelefonoCliente,CorreoCLiente)
            VALUES (?, ?, ?, ?, ?,?)
        ''', (self.identificacion, self.NombreCliente, self.ApellidoCliente, self.DireccionCliente, self.TelefonoCliente, self.CorreoCliente))
        
        DB.guardar()

    @staticmethod
    def ActualizarDir(DB, idcliente, nuevadir):

        DB.cursor.execute('''
            UPDATE clientes
            SET DireccionCliente = ?
            WHERE Identificacion = ?
        ''', (nuevadir, idcliente))

        DB.guardar()

    @staticmethod
    def Consultar(DB,idcliente):

        DB.cursor.execute("SELECT * FROM Clientes WHERE Identificacion = ?" , (idcliente))

        infocliente = DB.cursor.fetchone()

        print(infocliente)




db = BaseDeDatos() #Crea instancia de la base de datos (Solucion al problema de crear conexion cada vez que se opera)

cliente.Consultar(db,123)
