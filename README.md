# Gráficos en Python  
Se presenta un modulo desarrollado en Python para realizar gráficos de barras, así como también gráficos de torta.
La implementación se realiza utilizando el modulo Turtle disponible en Python, con programación procedural.

Las funciones para llamar a las funciones que permiten realizar los graficos se encuentran en sus respectivas carpetas cada uno donde cada uno contiene un archivo con el mismo nombre del directorio :
- grafico_de_barras
- grafico_de_tortas

Para poder utilizarlo se debe importar los archivos correspondientes a los graficos que queremos representar. Para poder importarlo desde un archivo por fuera del directorio donde se encuentra el programa que realiza el grafico, se debe respetar la siguiente sintaxis

directorio.archivo 

tener en cuenta que si se ejecuta desde un directorio externo se debe realizar todo el path del archivo, es decir

directorio.directorio.(...).archivo

las funciones principales las cuales se deben hacer invocación son:
- dibujar_grafico_barras
- dibujar_grafico_torta

# Uso de las funciones de Graficos

- ## dibujar_grafico_barras

Esta función recibe 4 tipos de parametros
datos = una lista de enteros indicando el valor de cada barra
etiquetas = una lista de strings indicando el nombre de cada barra
color = un string indicando el color de las barras
tiempo = un entero indicando el tiempo de visualizacion

se debe tener en cuenta que los datos y las etiquetas tienen que ser compatibles en cantidad, es decir que si se ingresa mas datos que etiquetas o viceversa el programa finalizará con codigo de error 1 imposibilitando su visualización

- ### Representación de valores de entrada e invocacion válidos 
```
datos = [20,30,40,50,60]
etiquetas = ["A","B","C","D","E"]
color = "blue"
tiempo = 5 

dibujar_grafico_barra(datos,etiquetas,color,tiempo)
```
Por defecto los parametros de color y tiempo se establecen el "red" y 3 respectivamente.
Para saber mas sobre la gamma de colores que se puede [ingresar aqui](http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter)


- ## dibujar_grafico_torta

Esta función recibe 3 tipos de parámetros:
datos = una lista de tuplas que contiene 2 valores cada una (string y entero) indicando la porcion a graficar
radio = un entero indicando el tamaño del radio de la circunferencia a representar
tiempo = un entero indicando el tiempo de visualizacion en segundos

- ### Representación de valores de entrada e invocacion válidos 
```
datos = [("Etiqueta A", 30), ("Etiqueta B", 15), ("Etiqueta C", 40), ("Etiqueta D", 10), ("Etiqueta E", 20)]
radio = 150
tiempo = 5

dibujar_grafico_torta(datos,radio,tiempo)

```
por defecto los parametros de radio y tiempo se establecen en 200 y 3 respectivamente


Puede encontrar un ejemplo de ejecucion de ambos graficos en el archivo [ejemplo.py](https://github.com/ucuraj/graficos_tortuga/blob/master/ejemplo.py)