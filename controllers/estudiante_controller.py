from database.conexion import database
from data.crud import crud
from models.estudiante import estudiante

class estudiante_controller:
    def __init__(self, vista, baseDatos, crud):
        self.vista = vista
        self.baseDatos = baseDatos
        self.crud = crud
        
    """Clase que maneja la información del estudiante entre la vista del programa y el modelo de negocio
    """    
    def main_menu_controller(self):
        """Metodo que consiste en un loop infinito para el metodo main_menu() de la vista y opcion().
        En este metodo se maneja la lógica de negocio manteniendo todo dentro de esta misma clase.

        """        
        while True:
            self.vista.main_menu()
            opcion = self.vista.opcion()
            
            if opcion == "1":
                self.crear_estudiante()
            
            elif opcion == "2":
                self.listar_estudiantes()
            
            elif opcion == "3":
                self.cambiar_nota()
            
            elif opcion == "4":
                self.eliminar_estudiante()
                
            elif opcion == "5":
                self.vista.mostrarMensaje("Saliendo del programa...")
                break
    
            else:
                self.vista.mostrarMensaje("Error, opcion invalida.")
                
    
    def crear_estudiante(self):
        """Clase que crea el estudiante 

        Args:
            nombre (str): nombre del estudiante
            correo (str): correo del estudiante
            nota (float): nota del estudiante
        """
        nombre, correo, nota = self.vista.pedir_datos_estudiante()
        newEstudiante = estudiante(None, nombre, correo, nota)
        
        self.crud.crear(newEstudiante)
        self.vista.mostrarMensaje("Creado con exito!")


    def listar_estudiantes(self):
        """Metodo para llamar la tabla y aplicarle la función de leer procedente de crud
        """    
        estudiantes = self.crud.leer()
        self.vista.mostrar_lista_estudiantes(estudiantes)
    
    def cambiar_nota(self):
        """Metodo que se encarga de llamar crud para actualizar la nota de un estudiante

        Args:
            nueva_nota (float): Nueva nota del estudiante
        """        
        id = self.vista.pedir_id()
        nueva_nota = self.vista.pedir_nueva_nota()
        self.crud.actualizar(id, nueva_nota)
        self.vista.mostrarMensaje("Modificado con exito!")
                

    def eliminar_estudiante(self):
        """Metodo que se encarga de pedir los datos necesarios y enviarlos al crud par eliminar un estudiante.
        """     
        id = self.vista.pedir_id()
        self.vista.mostrarMensaje(f'Esta seguro de eliminar al usuario con id: {id} (s/n): ')
        confirmacion = input()
        
        if confirmacion.lower() == "s":
            self.crud.eliminar(id)
            self.vista.mostrarMensaje("Estudiante eliminado correctamente. ")
        else: 
            self.vista.mostrarMensaje("Operacion cancelada...")
            return
        