# Gráficos en Python  
Estos módulos permiten crear gráficos de barras y de torta usando el módulo turtle de Python.

Las funciones que permiten crear los gráficos se encuentran en los archivos:
- [grafico_de_barras.py](https://github.com/ucuraj/graficos_tortuga/blob/master/grafico_de_barras/grafico_de_barras.py)
- [grafico_de_tortas.py](https://github.com/ucuraj/graficos_tortuga/blob/master/grafico_de_torta/grafico_de_torta.py)

Para poder utilizarlo en su programa debe importar el módulo correspondiente al tipo que gráfico que quiera utilizar:

import grafico_de_barras
import grafico_de_tortas

Las funciones principales que se deben invocar son:

- dibujar_grafico_barras
- dibujar_grafico_torta

## Uso de las funciones de Gráficos

### dibujar_grafico_barras

Esta función recibe 4 parámetros:
- **datos**: *una lista de enteros* indicando el valor de cada barra.
- **etiquetas** *(opcional)*: una *lista de strings* que representa el nombre de la etiqueta de cada barra. Si el parámetro no se encuentra, por defecto las etiquetas toman los siguientes valores: "Categoría 1",  "Categoría 2", …, "Categoría N". Siendo N la longitud de la lista datos.
- **color**: un *string* que representa el color de las barras. Si no se indica un color,  por defecto es "red". Los posibles colores se pueden consultar [ingresando aquí](http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter).
- **tiempo** *(opcional): un entero* que representa el tiempo de visualización en segundos. Si no se indica un tiempo, por defecto es 3.


Tener en cuenta que la cantidad de elementos de la lista datos debe ser igual al de la lista etiquetas, en caso contrario el programa finalizará con código de error 1, y por lo tanto no será posible visualizar el gráfico.

#### Posibles formas de invocación de la función dibujar_grafico_barra
##### Forma 1: Pasando todos los parámetros
```python
datos = [20,30,40,50,60]
etiquetas = ["A1","B2","C3","D4","E5"]
color = "blue"
tiempo = 5 

dibujar_grafico_barra(datos,etiquetas,color,tiempo)
```

##### Forma 2: Pasando solamente el parámetro obligatorio
Por defecto los parámetros etiquetas, color y tiempo se establecen en `["Categoría 1",  "Categoría 2", …, "Categoría N"] #siendo N la longitud de la lista datos`, `"red"` y `3` respectivamente. Son parámetros opcionales y pueden no estar presentes en la invocación:

`dibujar_grafico_barra(datos)`

# 
### dibujar_grafico_torta

Esta función recibe 3 parámetros:
- **datos**: una *lista de tuplas*. Cada tupla contiene los datos de una porción del gráfico de torta, y se compone de dos valores;  un string que representa el nombre de la etiqueta y un entero que es su valor asociado.
- **radio**: un *entero* que representa el tamaño del radio de la circunferencia. Si no se indica un valor de radio, por defecto es 200.
- **tiempo**: un *entero* un entero que representa el tiempo de visualización en segundos. Si no se indica un tiempo, por defecto es 3.

#### Posibles formas de invocación de la función dibujar_grafico_torta
##### Forma 1: Pasando todos los parámetros

```python
datos = [("Etiqueta A", 30), ("Etiqueta B", 15), ("Etiqueta C", 40), ("Etiqueta D", 10), ("Etiqueta E", 20)]
radio = 150
tiempo = 5
 
dibujar_grafico_torta(datos,radio,tiempo)
```

##### Forma 2: Pasando solamente el parámetro obligatorio
Por defecto los parámetros `radio` y `tiempo` se establecen en *200* y *3* respectivamente. Son parámetros opcionales y pueden no estar presentes en la invocación:

`dibujar_grafico_torta(datos)`

Puede encontrar un ejemplo de ejecucion de ambos graficos en el archivo [ejemplo.py](https://github.com/ucuraj/graficos_tortuga/blob/master/ejemplo.py)
