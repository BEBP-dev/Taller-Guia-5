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
        for fila in filas:
            est = estudiante(fila[1], fila[2], fila [3])
            est.id = fila[0]
            estudiantes.append(est)
        
        return estudiantes
        
        
    
    
    def actualizar(conn: sqlite3.Connection , id_estudiante: int , nueva_nota:float) -> None:
        """
        Actualiza la nota de un estudiante existente.
        conn: conexión activa a la base de datos
        id_estudiante: identificador del estudiante
        nueva_nota: nueva nota a asignar
        """
        conn.execute(
            "UPDATE estudiantes SET nota=? WHERE id=?",
            (nueva_nota , id_estudiante)
        )
        
        conn.commit ()

    def eliminar(conn: sqlite3.Connection , id_estudiante: int) -> None:
        """
        Elimina un estudiante de la base de datos.
        conn: conexión activa a la base de datos
        id_estudiante: identificador del estudiante a eliminar
        """
        conn.execute(
            "DELETE FROM estudiantes WHERE id=?",
            (id_estudiante ,)
        )
        
        conn.commit ()