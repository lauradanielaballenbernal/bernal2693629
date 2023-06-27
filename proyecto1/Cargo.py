class Cargo:
    def __init__(self, cuoc, nombre, descripcion, manual_funciones):
        self.__cuoc = cuoc
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__manual_funciones = manual_funciones

    
    def seCuoc(self,cuoc):
        self.__cuoc=cuoc
             
    def getCuoc(self):
        return self.__cuoc
    

    def setNombre(self,nombre):
        self.__nombre=nombre
             
    def getNombre(self):
        return self.__nombre
    

    def setDescripcion(self,descripcion):
        self.__descripcion=descripcion
             
    def getDescripcion(self):
        return self.__descripcion
    

    def setManual_funciones(self,manual_funciones):
        self.__manual_funciones=manual_funciones
             
    def getManual_funciones(self):
        return self.__manual_funciones