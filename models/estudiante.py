class estudiante:
    """Clase que se encarga de representar un estudiante.
        Incluye metodos getter para obtener la informacion del estudiante.
    """
    def __init__(self, id, nombre, correo, nota):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.nota = nota
    
    def getID(self):
        return self.id
    
    def getName(self):
        return self.nombre
    
    def getCorreo(self):
        return self.correo
    
    def getNota(self):
        return self.nota
    

