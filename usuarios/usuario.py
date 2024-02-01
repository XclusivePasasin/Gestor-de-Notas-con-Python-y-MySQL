import datetime 
import hashlib
import usuarios.conexion as conexion

# Variable Global Para Realizar Conexion
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    
    def __init__(self, nombre,apellido,email,contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
    
    def Registro(self): 
        fecha = datetime.datetime.now()
        # Ciframos La Contraseña Del Usuario
        cifrado = hashlib.sha256()
        cifrado.update(self.contraseña.encode('utf8'))
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        try:
            # Enviamos Los Datos
            cursor.execute(sql, usuario)
            database.commit() 
            resultado = [cursor.rowcount, self]
        except:
            resultado = [0,self]    
        return resultado    
        
    def Identificar(self):
        # Consulta Para Verificar Si El Usuario Existe 
        sql = "SELECT * FROM usuarios WHERE email = %s AND contraseña = %s"
         # Ciframos La Contraseña Del Usuario
        cifrado = hashlib.sha256()
        cifrado.update(self.contraseña.encode('utf8'))
        # Datos Para La Consulta
        usuario = (self.email, cifrado.hexdigest())
        # Enviamos Los Datos
        cursor.execute(sql,usuario)
        resultado = cursor.fetchone()
        
        return resultado