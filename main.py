from views.estudiante_view import estudiante_view
from controllers.estudiante_controller import estudiante_controller
from database.conexion import database
def main():
    """Metodo principal para ejecutar el programa
    """    
    vista = estudiante_view()
    baseDatos = database()
    controlador = estudiante_controller(vista,baseDatos)
    
    controlador.main_menu_controller()

if __name__ == "__main__":
    main()