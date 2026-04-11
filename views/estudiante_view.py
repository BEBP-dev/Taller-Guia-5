from controllers.estudiante_controller import estudiante_controller

class estudiante_view:
    """Clase estudiante_view, que maneja los menus necesarios del programa
    """
    @staticmethod          
    def main_menu(): 
        """Método main_menu, controla el menu principal que se le muestra al cliente al iniciar el programa
        """ 
        print("\n-- SISTEMA DE ESTUDIANTES --")
        print("1. Crear estudiante")
        print("2. Listar estudiante")
        print("3. Actualizar nota")
        print("4. Eliminar estudiante")
        print("5. Salir")
        print("-------------")

    def opcion(self):
        return input("Seleccione una opción: \n")

            

    @staticmethod
    def pedir_datos_estudiante():
        """Metodo que pide los datos del estudiante en la vista para crearlo
        """        
        nombre = input("Ingrese el Nombre del estudiante: ")
        correo = input("Ingrese el Correo del estudiante: ")
        nota = float(input("Ingrese la Nota del estudiante (en formato #.#): "))

        return nombre, correo, nota  

    @staticmethod
    def mostrar_lista_estudiantes(estudiantes):
        """Metodo para mostrar la lista de estudiantes de la tabla

        Args:
            estudiantes (estudiantes): apertura del database para poder leer los datos
        """        
        for estudiante in estudiantes:
            print(f'ID: {estudiante.getID()} - Nombre: {estudiante.getName()} - Correo: {estudiante.getCorreo()} - Nota: {estudiante.getNota()}')

    
    def pedir_nueva_nota(self):
        """Metodo que se encarga de pedir el ID de un estudiante al que se le necesite cambiar su nota, y pedir la nueva nota.
        """        
        nueva_nota = float(input("Nueva nota: "))

        return nueva_nota


    def mostrarMensaje(self, mensaje):
        print(mensaje)
    
    @staticmethod
    def pedir_id():
        return input("Ingresa el ID del estudiante para modificar/Eliminar: ")