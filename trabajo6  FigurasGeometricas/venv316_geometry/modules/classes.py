#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 2.0                         #
# Fecha: 11/06/2024                     #
#****************************************

# Este programa se diseño con el fin de colocar a prueba los conocimientos
# adquiridos en el tema de POO. A tres clases independientes se les introducen
# datos de su construccion y muestra los resultados en una tabla.

from math import pi

#----------------------TRIANGULO--------------------------------------
class Triangulo:

    def __init__(self, lado1, lado2, lado3): # Defino el constructor clase triangulo y sus atributos
        self.__lado1 = lado1
        self.__lado2 = lado2        # Funcion para la clase triangulo
        self.__lado3 = lado3
    
    
    def set_lado1(self, value):     # Defino el set lado1
        self.__lado1 = value
    
    def get_lado1(self):            # Defino el get lado1
        return self.__lado1
    
    def set_lado2(self, value):     # Defino el set lado2
        self.__lado2 = value

    def get_lado2(self):            # Defino el get lado2
        return self.__lado2         

    def set_lado3(self, value):     # Defino el set lado3
        self.__lado3 = value

    def get_lado3(self):
        return self.__lado3         # Defino el get lado3

    def validar_triangulo(self):  # Comprobamos la veracidad del triangulo que ingrese el usuario
     
        if not(self.__lado1 + self.__lado2 > self.__lado3 and
                self.__lado1 + self.__lado3 > self.__lado2 and
                self.__lado2 + self.__lado3 > self.__lado1):
            # Manejo de errores en el 
            # tiempo de ejecucion
            return ValueError("Los lados proporcionados no forman un triangulo válido")

    def print_area(self):
        print("lado1: ", self.get_lado1())
        print("lado2: ", self.get_lado2()) # Funcion para imprimir los lados 
        print("lado3: ", self.get_lado3())

    def perimetro (self):
        result = self.__lado1 + self.__lado2 + self.__lado3   
        return result     #Se realiza la funcion para hallar el perimetro del triangulo


    def area(self):       # Defino la función para hallar ela rea del triangulo  
        s = self.perimetro() / 2
        area = (s*(s - self.__lado1)*(s - self.__lado2)*(s - self.__lado3))**(1/2)
        return area 

#----------------------RECTANGULO--------------------------------------

class Rectangulo:
    def __init__(self, margen1, margen2, margen3, margen4): # Defino el constructor clase rectangulo y sus atributos
        self.__margen1 = margen1
        self.__margen2 = margen2
        self.__margen3 = margen3        # Funcion para la figura del rectangulo
        self.__margen4 = margen4
    
    def set_margen1(self, value):       # Defino el set margen1
        self.__margen1 = value
    
    def get_margen1(self):                          
        return self.__margen1           # Defino el get marge1
    
    def set_margen2(self, value):       # Defino el set margen2
        self.__margen2 = value
    
    def get_margen2(self):              # Defino el get marge2
        return self.__margen2

    def set_margen3(self, value):       # Defino el set margen3
        self.__margen3 = value
    
    def get_margen3(self):              # Defino el get marge3
        return self.__margen3

    def set_margen4(self, value):       # Defino el set margen4
        self.__margen4 = value
    
    def get_margen4(self):              # Defino el get margen4
        return self.__margen4
    

    def print_area(self):
        print("margen1: ", self.get_margen1())
        print("margen2: ", self.get_margen2()) # Funcion para imprimir los lados 
        print("margen3: ", self.get_margen3())
        print("margen4: ", self.get_margen4())
          

    def perimetro (self):
        return self.__margen1 + self.__margen2 + self.__margen3 + self.__margen4   
        #Se realiza la funcion para hallar el perimetro del rectangulo

    def area(self): 
        area = self.__margen1 * self.__margen4      # Defino el area
        return area 
        #Se realiza la funcion para hallar el area del rectangulo

 
            
#----------------------CIRCULO--------------------------------------

class Circulo:
 
    def __init__(self, radio): 
                self.__radio = radio            # Defino el constructor clase circulo y sus atributos

    def set_radio(self, value):                 # Defino el set de radio
        self.__radio = value
       
    
    def get_radio(self):
        return self.__radio                     # Defino el get de radio

    def print_area(self):
        print("radio: ", self.get_radio())

    def area(self): 
        s = pi * self.__radio * self.__radio    # Realizo la funcion para hallar el area del circulo
        return s
 
    def perimetro(self):
        perimetro = 2 * pi * self.__radio       # Realizo la funcion para hallar el perimetro del circulo
        return perimetro


