#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 2.0                         #
# Fecha: 11/06/2024                     #
#****************************************

# Este programa se diseño con el fin de colocar a prueba los conocimientos
# adquiridos en el tema de POO. A tres clases independientes se les introducen
# datos de su construccion y muestra los resultados en una tabla.


from modules import classes        #Importo el modulo functions donde estan los datos para imprimir la tabla 
from modules import functions     # Importo el modulo classes donde estan las funciones y operaciones 
from modules import menu 
from colorama import Fore,Back # Importo colorama para color fondo y fuente
print(Fore.BLACK + Back.RED)# Defino colores fondo y fuente 


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
      triangulo.validar_triangulo()
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