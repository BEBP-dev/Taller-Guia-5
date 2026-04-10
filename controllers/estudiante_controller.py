from database.conexion import database
from data.crud import crud
from models.estudiante import estudiante

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
                    from views.estudiante_view import estudiante_view
                    estudiante_view.pedir_datos_estudiante()
                    return False
                case 2:
                    listar_estudiantes()
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
    
    
    def crear_estudiante(nombre, correo, nota):
        """Clase que crea el estudiante 

        Args:
            nombre (str): nombre del estudiante
            correo (str): correo del estudiante
            nota (float): nota del estudiante
        """
        newEstudiante = estudiante(nombre, correo, nota)
        conn = database.conectar()
        database.crear_tabla(conn)

        crud.crear(conn, newEstudiante)

    def listar_estudiantes():
        """Metodo para llamar la tabla y aplicarle la función de leer procedente de crud
        """    
        conn = database.conectar()

        estudiantes = crud.leer(conn)
        from views.estudiante_view import estudiante_view
        estudiante_view.mostrar_lista_estudiantes(estudiantes)

