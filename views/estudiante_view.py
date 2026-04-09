from controllers.estudiante_controller import estudiante_controller

class estudiante_view():

    def main_menu(): 
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
