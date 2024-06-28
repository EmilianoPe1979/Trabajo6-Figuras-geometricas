#***************************************#
# CENTRO DE BIOTECNOLOGIA AGROPECUARIA  #
# NOMBRE EMILIANO PERILLA AGUILAR       #
# VERSION : 2.0                         #
# Fecha: 11/06/2024                     #
#****************************************

# Este programa se diseño con el fin de colocar a prueba los conocimientos
# adquiridos en el tema de POO. A tres clases independientes se les introducen
# datos de su construccion y muestra los resultados en una tabla.

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

  

  