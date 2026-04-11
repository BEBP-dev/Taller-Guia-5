import sqlite3
class database:
    def __init__(self):
        self.connection = sqlite3.connect("estudiantes.db")
        self.cursor = self.connection.cursor()
        self.crear_tabla()
    
    def crear_tabla(self):
        self.cursos.execute(
            """CREATE TABLE IF NOT EXISTS estudiantes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                correo TEXT,
                nota REAL
                )"""
        )
        self.connection.commit()