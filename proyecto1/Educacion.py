class Educacion:
    def __init__(self, institucion, fecha_inicio, fecha_fin, tipo_educacion):
        self.__institucion = institucion
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__tipo_educacion = tipo_educacion

    def setInstitucion(self, institucion):
        self.__institucion = institucion

    def getInstitucion(self):
        return self.__institucion
    

    def setFecha_inicio(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio
   
    def getFecha_inicio(self):
        return self.__fecha_inicio
    

    def setFecha_fin(self,fecha_fin):
        self.__fecha_fin = fecha_fin

    def getFecha_fin(self):
        return self.__fecha_fin
    

    def setTipo_educacion(self,tipo_educacion):
        self.__tipo_educacion = tipo_educacion
   
    def getTipo_educacion(self):
        return self.__tipo_educacion
