import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    
    def Registrarse(self):
        print('\nOk, Vamos a registrarte en el sistema!!!')
        #Solicitar Datos Personales Al Usuario
        nombre = input('Ingrese su nombre: ')
        apellido = input('Ingrese su Apellido: ')
        email = input('Introduzca su correo electronico: ')
        contraseña = input('Introduzca una contraseña:  ')
        # Enviamos Datos 
        usuario = modelo.Usuario(nombre,apellido,email,contraseña)
        registro = usuario.Registro()
        
        if registro[0] >= 1:
            print(f"\nPerfecto!, {registro[1].nombre} te has registrado con el email: {usuario.email}")
        else:
            print(f"\nNo te has registrado correctamente!!!")
        
    def IniciarSesion(self):
        print('\nOk, Ingrese sus credenciales de acceso!!!')
        try:
            # Solicitamos Datos De Acceso Al Usuario
            email = input('Introduzca su correo electronico: ')
            contraseña = input('Introduzca su contraseña:  ')
            
            usuario = modelo.Usuario('','',email,contraseña)
            Validacion = usuario.Identificar()

            if email == Validacion[3]:
                print(f"Bienvenido {Validacion[1]} te has registrado en el {Validacion[5]}")
                self.proximasAcciones(Validacion)
        except Exception as error:
            print(f"Inicio De Sesion Incorrecto! Intentalo mas tarde.")
            
    def proximasAcciones(self, usuario):
        print("""
Acciones Disponibles:
- Crear Notas (Crear)
- Mostrar Notas (Mostrar)
- Eliminar Notas (Eliminar)
- Salir (Salir)
        """)
        
        accion = input("Que Deseas Realizar: ")
        accionesNotas = notas.acciones.Acciones()
            
        if accion == "Crear":
            accionesNotas.CrearNota(usuario)
            self.proximasAcciones(usuario)
        elif accion == "Mostrar":
            accionesNotas.MostrarNota(usuario)
            self.proximasAcciones(usuario)
        elif accion == "Eliminar":
            accionesNotas.EliminarNota(usuario)
            self.proximasAcciones(usuario)
        elif accion == "Salir":
            print(f'Ok, {usuario[1]} Hasta Pronto!!!')
            exit()            