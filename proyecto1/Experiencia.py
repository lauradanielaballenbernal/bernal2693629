class Experiencia:
    def __init__(self,empresa,descripcion,fecha_inicio,fecha_fin,cargo,funciones):
        self.__empresa = empresa
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__cargo = cargo
        self.__funciones = funciones
        
    def setEmpresa(self,empresa):
        self.__empresa = empresa
   
    def getEmpresa(self):
        return self.__empresa
    
    
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion
             
    def getDescripcion(self):
        return self.__descripcion
    
    
    def setfecha_inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio
            
    def getfecha_inicio(self):
        return self.__fecha_inicio
    
    
    def setFecha_fin(self, fecha_fin):
        self.__fecha_fin = fecha_fin
        
    def getFecha_fin(self):
        return self.__fecha_fin
    
    
    def setCargo(self,cargo):
        self.__cargo = cargo
         
    def getCargo(self):
        return self.__cargo
    
    
    def setfunciones(self,funciones):
        self.__funciones = funciones
         
    def getfunciones(self):
        return self.__funciones
   