# Gráficos en Python  
Se presenta un modulo desarrollado en Python para realizar gráficos de barras, así como también gráficos de torta.
La implementación se realiza utilizando el modulo Turtle disponible en Python, con programación procedural.

Las funciones que permiten realizar los gráficos se encuentran en sus respectivas carpetas, donde cada uno contiene un archivo con el mismo nombre del directorio:
- grafico_de_barras
- grafico_de_tortas

Para poder utilizarlo se deben importar los archivos correspondientes a los graficos que deseamos representar. 
La importación desde un archivo que se aloje fuera del directorio donde se encuentre el programa que realiza el gráfico, debe respetar la siguiente sintáxis:
directorio.archivo 

Tener en cuenta que si se ejecuta desde un directorio externo se debe colocar todo el path del archivo:
directorio.directorio.(...).archivo

Las funciones principales que se deben invocar son:
- dibujar_grafico_barras
- dibujar_grafico_torta

# Uso de las funciones de Graficos

- ## dibujar_grafico_barras

Esta función recibe 4 tipos de parámetros:
datos = una lista de enteros indicando el valor de cada barra
etiquetas = una lista de strings indicando el nombre de cada barra
color = un string indicando el color de las barras (opcional, por defecto es "red")
tiempo = un entero indicando el tiempo de visualizacion (opcional, por defecto es 3)

Se debe tener en cuenta que tanto los datos como las etiquetas deben ser compatibles en cantidad, es decir, si se ingresan mayor cantidad de datos que de etiquetas o viceversa, el programa finalizará con código de error 1 imposibilitando su visualización.

- ### Representación de valores de entrada e invocacion válidos 
```
datos = [20,30,40,50,60]
etiquetas = ["A1","B2","C3","D4","E5"]
color = "blue"
tiempo = 5 

dibujar_grafico_barra(datos,etiquetas,color,tiempo)
```
Por defecto los parámetros de etiquetas, color y tiempo se establecen en "Categoria n" (siendo n=1..longitud de la lista llamada datos), "red" y 3 respectivamente. De este modo, dichos parámetros se vuelven opcionales, haciendo válida la invocación de la función obviando dichos valores:

dibujar_grafico_barra(datos)
  
Para saber mas sobre la gamma de colores que se pueden utilizar [ingresar aqui](http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter)


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
Por defecto los parametros de radio y tiempo se establecen en 200 y 3 respectivamente. De este modo, dichos parámetros se vuelven opcionales, haciendo válida la invocación de la función obviando dichos valores:
dibujar_grafico_torta(datos)



Puede encontrar un ejemplo de ejecucion de ambos graficos en el archivo [ejemplo.py](https://github.com/ucuraj/graficos_tortuga/blob/master/ejemplo.py)
