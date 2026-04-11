from controllers.estudiante_controller import estudiante_controller

class estudiante_view():
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

    @staticmethod
    def pedir_nueva_nota():
        """Metodo que se encarga de pedir el ID de un estudiante al que se le necesite cambiar su nota, y pedir la nueva nota.
        """        
        id_estudiante = int(input("ID: "))
        nueva_nota = float(input("Nueva nota: "))

        return id_estudiante, nueva_nota

    @staticmethod
    def pedir_eliminar_estudiante():
        """Metodo que se encarga de pedir el ID del estudiante a eliminar de la lista
        """        
        id_estudiante = int(input("ID: "))

        estudiante_controller.eliminar_estudiante(id_estudiante)
        
    def mostrarMensaje(self, mensaje):
        print(mensaje)
    