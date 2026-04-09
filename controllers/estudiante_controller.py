from views.estudiante_view import estudiante_view

class estudiante_controller:
    """Clase que maneja la información del estudiante entre la vista del programa y el modelo de negocio
    """    
    def main_menu_controller(option):
        """Método que maneja la información obtenida en el menu principal y la conecta con el modelo de negocio

        Args:
            option (int): Opción elegida por el usuario en la vista

        Returns:
            boolean: Returns utilizados para informar a la vista sobre el paso a seguir en el programa
        """        

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