from views.estudiante_view import estudiante_view
from controllers.estudiante_controller import estudiante_controller
from database.conexion import database
from data.crud import crud
def main():
    """Metodo principal para ejecutar el programa
    """    
    vista = estudiante_view()
    baseDatos = database()
    crudo = crud(baseDatos)
    controlador = estudiante_controller(vista,baseDatos, crudo)
    
    controlador.main_menu_controller()

if __name__ == "__main__":
    main()