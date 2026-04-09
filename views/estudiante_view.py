from controllers.estudiante_controller import estudiante_controller

class estudiante_view():
    """Clase estudiante_view, que maneja los menus necesarios del programa
    """          
    def main_menu(): 
        """Método main_menu, controla el menu principal que se le muestra al cliente al iniciar el programa
        """ 
        option = 0
        while True:

            print("\n-- SISTEMA DE ESTUDIANTES --")
            print("1. Crear estudiante")
            print("2. Listar estudiante")
            print("3. Actualizar nota")
            print("4. Eliminar estudiante")
            print("5. Salir")
            print("-------------")

            option = input("Seleccione una opción: \n")

            verificate=estudiante_controller.main_menu_controller(option)

            if verificate:
                break
