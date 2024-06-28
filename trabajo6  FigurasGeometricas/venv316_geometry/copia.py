def main():

  while True:
    print("-----------------------")
    print("FIGURAS GEOMETRICAS")
    print("1. Triangulo")
    print("2. circulo")             # Defino el menu de operaciones del programa 
    print("3. Rectangulo")          # Al escoger un numero del 1 al 4 el usuario
    print("4. Imprimir")            # Puede definir las entrdas de cada figura 
    print("5. Salir")
    print("-----------------------")
    opcion = int(input("Escoge una opcion: ")) # El usuario escoge una opcion 

    if opcion == 1:
      lado1 = int(float(input ("Ingrese el lado1: ")))
      lado2 = int(float(input ("Ingrese el lado2: ")))   # Opcion para ingresar los lados del triangulo 
      lado3 = int(float(input ("Ingrese el lado3: ")))

      triangulo = classes.Triangulo(lado1,lado2,lado3)
      area_total_triangulo = triangulo.print_area()
      # print("este es el resultado del area",triangulo.area())
      # print("este es el resultado del perimetro",triangulo.perimetro())

    elif opcion== 2:
      radio = int(float(input ("Ingrese radio: ")))
      circulo = classes.Circulo(radio)
      area_total_circulo = circulo.print_area()        # Opcion para ingresar el radio del circulo 
      # radio = print("este es el resultado del area del radio",circulo.area())
      # perimetro = print("este es el resultado del perimetro",circulo.perimetro())

    elif opcion== 3:
      margen1 = int(float(input ("Ingrese margen1: ")))
      margen2 = int(float(input ("Ingrese margen2: "))) # Opcion pra ingresar los lados del rectangulo 
      margen3 = int(float(input ("Ingrese margen3: ")))
      margen4 = int(float(input ("Ingrese margen4: ")))

      rectangulo = classes.Rectangulo(margen1,margen2,margen3,margen4)

      area_total_rectangulo = rectangulo.print_area()
      # print("este es el resultado del area",rectangulo.area())
      # print("este es el resultado del perimetro",rectangulo.perimetro())

    elif opcion== 4:
      functions.imprimir(triangulo,circulo,rectangulo)  # Opcion para imprimir la tabla 

    elif opcion== 5:
      print("Adios")     # Opcion para salir del programa  
      break              # Opcion para romper el ciclo
    else:
      print("Opcion no valida")

if __name__ == "__main__":
  main()

from modules import classes        #Importo el modulo functions donde estan los datos para imprimir la tabla 
from modules import functions     # Importo el modulo classes donde estan las funciones y operaciones 
from colorama import Fore,Back # Importo colorama para color fondo y fuente
print(Fore.BLACK + Back.RED)# Defino colores fondo y fuente 

def main(): # Defino la funcion del progrma principal

 while True:
    print("-----------------------")
    print("FIGURAS GEOMETRICAS")
    print("1. Triangulo")
    print("2. circulo")             # Defino el menu de operaciones del programa 
    print("3. Rectangulo")          # Al escoger un numero del 1 al 4 el usuario
    print("4. Imprimir")            # Puede definir las entrdas de cada figura 
    print("5. Salir")
    print("-----------------------")
    while True:
      try:
          opcion = int(input("Escoge una opción: "))
          break  # Salimos del bucle si se ingresa un número válido
      except ValueError:
          print("Opción inválida. Inténtalo nuevamente.")
    # opcion = int(input("Escoge una opcion: ")) # El usuario escoge una opcion 

    if opcion == 1:
      while True:  # Opcion para ingresar los lados del triangulo
        try:
          lado1 = float(input ("Ingrese el lado1: ")) # Ingresa lado1
          break
        except ValueError: # Si ingresa un caracter le captura el error y le muestra el mensaje
          print("No puede ingresar caracteres alfabeticos") 

      while True:               
        try:
          lado2 = float(input ("Ingrese el lado2: ")) # Ingrese lado2
          break
        except ValueError: # Si ingresa un caracter le captura el error y le muestra el mensaje
          print("No puede ingresar caracteres alfabeticos") 
      
      while True: 
        try:
          lado3 = float(input ("Ingrese el lado3: ")) # Ingrese lado3
          break
        except ValueError: # Si ingresa un caracter le captura el error y le muestra el mensaje
          print("No puede ingresar caracteres alfabeticos")   

      triangulo = classes.Triangulo(lado1,lado2,lado3)
      area_total_triangulo = triangulo.print_area()
      # print("este es el resultado del area",triangulo.area())
      # print("este es el resultado del perimetro",triangulo.perimetro())

      
    elif opcion== 2:
      
      while True:  # Opcion para ingresar los lados del triangulo
        try:
          radio = float(input ("Ingrese el radio: ")) # Ingresa lado1
          break
        except ValueError: # Si ingresa un caracter le captura el error y le muestra el mensaje
          print("No puede ingresar caracteres alfabeticos") 
      circulo = classes.Circulo(radio)
      area_total_circulo = circulo.print_area()        # Opcion para ingresar el radio del circulo 
      # radio = print("este es el resultado del area del radio",circulo.area())
      # perimetro = print("este es el resultado del perimetro",circulo.perimetro())

    elif opcion== 3:

      while True:               
        try:
          margen1 = float(input ("Ingrese margen1: ")) # Ingrese margen1
          break
        except ValueError: # Si ingresa un caracter le captura el error y le muestra el mensaje
          print("No puede ingresar caracteres alfabeticos") 

      while True:               
        try:
          margen2 = float(input ("Ingrese margen2: ")) # Ingrese margen2
          break
        except ValueError: # Si ingresa un caracter le captura el error y le muestra el mensaje
          print("No puede ingresar caracteres alfabeticos") 

      while True:               
        try:
          margen3 = float(input ("Ingrese margen3: ")) # Ingrese margen3
          break
        except ValueError: # Si ingresa un caracter le captura el error y le muestra el mensaje
          print("No puede ingresar caracteres alfabeticos") 

      while True:               
        try:
          margen4 = float(input ("Ingrese margen4: ")) # Ingrese margen3
          break
        except ValueError: # Si ingresa un caracter le captura el error y le muestra el mensaje
          print("No puede ingresar caracteres alfabeticos") 

      rectangulo = classes.Rectangulo(margen1,margen2,margen3,margen4)
      area_total_rectangulo = rectangulo.print_area()
      # print("este es el resultado del area",rectangulo.area())
      # print("este es el resultado del perimetro",rectangulo.perimetro())

    elif opcion== 4:
      functions.imprimir(triangulo,circulo,rectangulo)  # Opcion para imprimir la tabla 

    elif opcion== 5:
      print("Adios")     # Opcion para salir del programa  
      break              # Opcion para romper el ciclo
    else:
      print("Opcion no valida")

if __name__ == "__main__":
  main()

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


def imprimir(triangulo,circulo,rectangulo): # Funcion para imprimir la tabla 
    tabla = """ 
+--------------------------------------------------------------------------------------------------+
|                                    FIGURAS GEOMETRICAS                                           |
|--------------------------------------------------------------------------------------------------|    
|   Figura             Parametros                             Area           Perimetro             |
|--------------------------------------------------------------------------------------------------|
"""
    param_rect = 'margen1 {0} margen2 {1} margen3 {2} margen4 {3}'.format(format(rectangulo.get_margen1(), '.2f'), 
    format(rectangulo.get_margen2(), '.2f'), format(rectangulo.get_margen3(), '.2f'), format(rectangulo.get_margen4(), '.2f'))
    param_circ = 'radio {0}'.format(format(circulo.get_radio(), '.2f'))
    param_tria = 'lado1: {0} lado2: {1} lado3: {2}'.format(format(triangulo.get_lado1(), '.2f'),
                                                                    format(triangulo.get_lado2(), '.2f'),   
                                                                    format(triangulo.get_lado3(), '.2f'))
    # Estos son los prametros de la subicaiones de donde va a quedar la informacion de las figuras 
    # Se delimitan las margenes de la tabla principal
    # Con los get que vienen de las clase se traen los resultados de cada figura

    tabla = tabla + '{4}{0:<15s} {1:<55s} {2:<10s} {3:14s} {4}\n'.format(
            'Rectangulo', param_rect, format(rectangulo.area(), '.2f'),     # Datos de ubicacion información rectangulo
              format(rectangulo.perimetro(), '.2f'),'|')

    tabla = tabla + '{4}{0:<15s} {1:<55s} {2:<10s} {3:14s} {4}\n'.format(
            'Circulo', param_circ, format(circulo.area(), '.2f'),           #Datos de ubicacion información circulo
             format(circulo.perimetro(), '.2f'),'|')

    tabla = tabla + '{4}{0:<15s} {1:<55s} {2:<10s} {3:14s} {4}\n'.format(
             'Triangulo', param_tria, format(triangulo.area(), '.2f'),  # Datos de ubicacion información triangulo 
                format(triangulo.perimetro(), '.2f'),'|')

    tabla = tabla + "+--------------------------------------\
------------------------------------------------------------+\n"
    print(tabla) # El print de toda la tabla una vez estabeciso las ubicaciones y resultados 

  