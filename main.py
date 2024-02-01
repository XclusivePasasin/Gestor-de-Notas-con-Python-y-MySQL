"""
Proyecto Python y MySQL:
- Abrir Asistente
- Login o Registro
- Si elegimos registro, creará un usuario en la base de datos
- Si elegimos Login, Identifica al usuario y nos preguntará 
- Crear Nota, Mostrar Nota, Borrarlas.
"""

from usuarios import acciones

# Variable Global Para Ejecutar Las Funciones Del Modulo
Inicio = acciones.Acciones()

print(
"""
Acciones Disponibles:
1) Registro
2) Iniciar Sesion    
"""
)
# Pedimos La Accion Que El Usuario Quiera Realizar
accion = input("¿Que quieres realizar? ")

if accion == 'Registro':
    Inicio.Registrarse()

        
elif accion == 'Iniciar Sesion':
    Inicio.IniciarSesion()