import sqlite3
from models.estudiante import estudiante
class crud:
    """
    Módulo de operaciones CRUD para la gestión de estudiantes.
    Contiene funciones para crear , consultar , actualizar y eliminar
    registros en la base de datos SQLite.
    """
    def __init__(self, database):
        """Constructor

        Args:
            database (database): usamos este atributo para mantener un bajo acoplamiento y asi mismo
            trabajar sobre la base de datos.
        """
        self.db = database
        
    def crear(self, estudiante):

        """
        Inserta un nuevo estudiante en la base de datos.
        """
        self.db.cursor.execute(
            "INSERT INTO estudiantes (nombre, correo, nota) VALUES (?, ?, ?)",
            (estudiante.getName(), estudiante.getCorreo(), estudiante.getNota())
        )
        self.db.connection.commit ()

    def leer(self):
        """
        Consulta todos los estudiantes registrados.

        """
        filas = self.db.cursor.execute("SELECT id, nombre, correo, nota FROM estudiantes")

        estudiantes = []
        for id_, nombre, correo, nota in filas:
            est = estudiante(id_, nombre, correo, nota)
            estudiantes.append(est)
        
        return estudiantes
        
        
    def actualizar(self, id, nueva_nota):
        
        """
        Actualiza los datos de un estudiante registrado en la base de datos.
        """
        self.db.cursor.execute("""
            UPDATE estudiantes
            SET nota = ?
            WHERE id = ?
            """,
            (nueva_nota, id)
        )
        self.db.connection.commit()
        
        

    def eliminar(self, id):
        """
        Elimina un estudiante de la base de datos.
        id_estudiante: identificador del estudiante a eliminar
        """
        self.db.connection.execute(
            "DELETE FROM estudiantes WHERE id=?",
            (id ,)
        )
        
        self.db.connection.commit ()