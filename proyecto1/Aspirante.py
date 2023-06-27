from Usuario import *
from Experiencia import *
from Educacion import *
class Aspirante(Usuario):
    def __init__(self, documento, nombre, correo, contraseña,telefono, ubicacion):
        Usuario.__init__(self,documento,nombre, correo, contraseña, telefono, ubicacion)
        self.__documento = documento
        self.__nombre  = nombre
        self.__correo = correo
        self.__contraseña = contraseña
        self.__telefono = telefono
        self.__experiencia = []
        self.__educacion = []
        self.__ubicacion = ubicacion
        self.__aspirante = []
    def setDocumento(self,documento):
        self.__documento = documento 
   
    def getDocumento(self):
        return self.__documento
    
    
    def setNombre(self,nombre):
        self.__nombre=nombre
             
    def getNombre(self):
        return self.__nombre
    
    
    def setCorreo(self,correo):
        self.__correo = correo
            
    def getCorreo(self):
        return self.__correo
    
    
    def setContraseña(self,contraseña):
        self.__contraseña = contraseña
        
    def getContraseña(self):
        return self.__contraseña
    
    
    def setTelefono(self,telefono):
        self.__telefono = telefono
         
    def getTelefono(self):
        return self.__telefono
    
    
    def componerExperiencia(self):
        empresa=input('Ingrese nombre de la empresa: ')
        descripcion=input('Ingrese la descripcion de la experiencia: ')
        fecha_inicio=input('Ingrese la fecha de inicio de la experiencia: ')
        fecha_fin=input('Ingrese la fecha de finalizacion de la experiencia: ')
        cargo=input('Ingrese el cargo que desempeño durante la experiencia: ')
        funciones=input('Ingrese las funciones que hacia durante la experiencia: ')
        objexperiencia=Experiencia(empresa, descripcion, fecha_inicio, fecha_fin, cargo, funciones)
        self.__experiencia.append(objexperiencia)

    def verExperiencia(self):
        return self.__experiencia


    def componerEducacion(self):
        institucion =input('Ingrese el nombre de la institucion: ')
        fecha_inicio=input('Ingrese la fecha de inicio de la educacion: ')
        fecha_fin=input('Ingrese la fecha de finalizacion de la educacion: ')
        tipo_educacion=input('Ingrese el tipo de educacion: ')
        objeducacion = Educacion(institucion, fecha_inicio, fecha_fin, tipo_educacion)
        self.__educacion.append(objeducacion)
    
    def verEducacion(self):
        return self.__educacion
    

    def setUbicacion(self,ubicacion):
        self.__ubicacion = ubicacion
         
    def getTelefono(self):
        return self.__ubicacion
    


    def componerAspirante(self):
        documento = input("Ingrese su número de documento: ")
        nombre = input("Ingrese su nombre completo: ")
        correo = input("Ingrese su correo electrónico: ")
        contraseña = input("Ingrese una contraseña: ")
        telefono = input("Ingrese su número de teléfono: ")
        ubicacion = input("Ingrese su ubicación: ")

        aspirante = Aspirante(documento, nombre, correo, contraseña, telefono, ubicacion)
        Aspirante.aspirantelista.append(aspirante)
    
    
    def verAspirante(self):
        return self.aspirantelista