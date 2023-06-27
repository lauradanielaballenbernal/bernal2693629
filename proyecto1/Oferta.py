from Cargo import *
class Oferta:
    def __init__(self,nombre, tipo_contrato, n_vacantes, n_postulaciones, salario, tipo_empleo):
        self.__nombre = nombre
        self.__tipo_cotrato = tipo_contrato
        self.__cargo = []
        self.__n_vacantes = n_vacantes
        self.__n_postulaciones = n_postulaciones
        self.__salario = salario
        self.__tipo_empleo = tipo_empleo


    def setNombre(self,nombre):
        self.__nombre=nombre
             
    def getNombre(self):
        return self.__nombre
    

    def setTipo_contrato(self,tipo_contrato):
        self.__tipo_cotrato=tipo_contrato
             
    def getNombre(self):
        return self.__tipo_cotrato
    

    def componerCargo(self):
        cuoc=input('Ingrese el cual asociado al cargo: ')
        nombre=input('Ingrese el nombre del cargo: ')
        descripcion=input('Ingrese la descripcion del cargo: ')
        manual_funciones=input('Ingrese las funciones del cargo: ')
        objcargo=Cargo(cuoc,nombre,descripcion,manual_funciones)
        self.__cargo.append(objcargo)


    def setN_vacantes(self,n_vacantes):
        self.__n_vacantes=n_vacantes
             
    def getN_vacantes(self):
        return self.__n_vacantes
    

    def setN_postulaciones(self,n_postulaciones):
        self.__n_postulaciones=n_postulaciones
             
    def getN_postulaciones(self):
        return self.__n_postulaciones
    

    def setN_postulaciones(self,n_postulaciones):
        self.__n_postulaciones=n_postulaciones
             
    def getN_postulaciones(self):
        return self.__n_postulaciones
    

    def setSalario(self,salario):
        self.__salario=salario
             
    def getSalario(self):
        return self.__salario
    

    def setTipo_empleo(self, tipo_empleo):
        self.__tipo_empleo=tipo_empleo
             
    def getN_postulaciones(self):
        return self.__tipo_empleo
    
    def aumentar_postulaciones(self, n_postulaciones):
        n_postulaciones += 1