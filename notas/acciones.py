import notas.nota as modelo

class Acciones:
    
    def CrearNota(self, usuario):
        print(f'\nOk {usuario[1]} Vamos a crear una nota nueva...')
        titulo = input('Introduce el titulo de tu nota: ')
        descripcion = input('Introduce el contenido de tu nota: ')
        
        nota = modelo.Notas(usuario[0], titulo, descripcion)
        guardar = nota.GuardarNota()
        if guardar[0] >= 1:
            print(f'\nPerfecto, Has guardado la nota: {nota.titulo}')
        else:
            print(f'No se ha guardado la nota, losiento {usuario[1]}')
            
    def MostrarNota(self, usuario):
        print(f"\nVale {usuario[1]}!! Aqui tienes tus notas: ")
        nota = modelo.Notas(usuario[0])
        notas = nota.ListarNotas()
        
        for nota in notas:
            print("==================================")
            print(f'Numero Nota: {nota[0]}')
            print(f'Titulo: {nota[2]}')
            print(f'Descripción: {nota[3]}')
            print("==================================\n")
            
    def EliminarNota(self, usuario):
        print(f'\nOk {usuario[1]} Vamos a eliminar una nota...')
        titulo = input('Introduce el titulo de tu nota que deseas eliminar: ')
        nota = modelo.Notas(usuario[0], titulo)
        eliminar = nota.BorrarNotas()
        if eliminar[0] >= 1:
            print(f'\nPerfecto, Has eliminado la nota: {nota.titulo}')
        else:
            print(f'No se ha eliminado la nota, losiento {usuario[1]}')