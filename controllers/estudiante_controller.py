from views.estudiante_view import estudiante_view

class estudiante_controller:
    def main_menu_controller(option):

        try:
            option=int(option)

            match(option):
                case 1:
                    print()
                    return False
                case 2:
                    print()
                    return False
                case 3:
                    print()
                    return False
                case 4: 
                    print()
                    return False
                case 5:
                    print("Saliendo del programa.....")
                    return True
                case _:
                    print("Opción invalida, igrese un número del 1 al 5")
                    return False

        except ValueError:
            print("Opción invalida, igrese un número del 1 al 5")
            return False