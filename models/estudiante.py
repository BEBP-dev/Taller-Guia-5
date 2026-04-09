class estudiante:
    """Clase que se encarga de representar un estudiante.
        Incluye metodos getter para obtener la informacion del estudiante.
    """
    def __init__(self, nombre, correo, nota):
        self.nombre = nombre
        self.correo = correo
        self.nota = nota
    
    def getName(self):
        return self.nombre
    
    def getCorreo(self):
        return self.correo
    
    def getNota(self):
        return self.nota
    

