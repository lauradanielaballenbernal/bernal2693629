from Usuario import *
from Oferta import *
class Empresa(Usuario):
    listaofertas = []
    def __init__(self, documento, nombre, correo, contraseña, telefono,ubicacion):
        Usuario.__init__(documento, nombre, correo, contraseña, telefono, ubicacion)
        self.__documento = documento
        self.__nombre  = nombre
        self.__correo = correo
        self.__contraseña = contraseña
        self.__telefono = telefono
        self.__oferta = []
        self.__ubicacion = ubicacion


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
    
    
    def componerOferta(self):
        nombre=input('Ingrese nombre de la oferta: ')
        tipo_contrato=input('Ingrese el tipo de contrato de la oferta: ')
        n_vacantes=input('Ingrese el numero de vacantes disponibles: ')
        n_postulaciones=input('Ingrese los aspirantes que se han postulado: ')
        salario=input('Ingrese el salario ofrecido: ')
        tipo_empleo=input('Ingrese el tipo de empleo: ')
        objoferta=Oferta(nombre, tipo_contrato, n_vacantes, n_postulaciones, salario, tipo_empleo)
        Empresa.listaofertas.append(objoferta)

    def verOferta(self):
        return self.__oferta
    

    def setUbicacion(self,ubicacion):
        self.__ubicacion = ubicacion
         
    def getTelefono(self):
        return self.__ubicacion
    



    def componerEmpresa(self):
        documento = input("Ingrese su número de documento: ")
        nombre = input("Ingrese su nombre completo: ")
        correo = input("Ingrese su correo electrónico: ")
        contraseña = input("Ingrese una contraseña: ")
        telefono = input("Ingrese su número de teléfono: ")
        ubicacion = input("Ingrese su ubicación: ")

        empresa = Empresa(documento, nombre, correo, contraseña, telefono, ubicacion)
        Empresa.empresalista.append(empresa)
    
     
    def verEmpresa(self):
        return self.empresalista