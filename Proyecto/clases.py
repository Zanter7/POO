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

        DB.cursor.execute("SELECT * FROM Clientes WHERE Identificacion = ?" , (idcliente,)) # "," idcliente es importante

        infocliente = DB.cursor.fetchone()

        return infocliente




db = BaseDeDatos() #Crea instancia de la base de datos (Solucion al problema de crear conexion cada vez que se opera)

cliente.Consultar(db,1011322256)


while True: #ciclo de prueba

    print("bienvenido a la DB de clientes")
    print("Que desea hacer ?")
    print("Digite: ")
    print("1. Para crear un nuevo cliente")
    print("2. para editar la direccion de un cliente")
    print("3. Para consultar sobre un cliente")
    print("4. para salir")

    control = int(input())

    if control>4:
        print("Numero no disponible")
        continue

    if control == 1:
        a = input("ID Cliente: ")
        b = input("nombre Cliente: ")
        c = input("Apellido Cliente: ")
        d = input("direccion Cliente: ")
        e = input("telefono Cliente: ")
        f = input("correo Cliente: ")
        clienteN = cliente(a,b,c,d,e,f)
        clienteN.CrearCliente(db)
    
    if control == 2:
        cliente.ActualizarDir(db,input("ingrese identificacion a editar numero cliente:"), input("ingrese nueva direccion:"))
        print("hecho")

    if control == 3:
        print(cliente.Consultar(db,input("id cliente a consultar:")))
    
    if control == 4:
        db.guardar()
        db.CerrarConexion()
        print("desconectao")
        break
