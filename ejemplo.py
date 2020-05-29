import turtle
from grafico_de_barras import dibujar_grafico_barras
from grafico_de_torta import dibujar_grafico_torta

##### Grafico de barras
datos = [10, 20, 30, 20, 10]
etiqueta = ["A1", "B2", "C3", "D4", "E5"]
dibujar_grafico_barras(datos, etiqueta, color="green")

##### Grafico de torta
datos = [("Etiqueta A", 30), ("Etiqueta B", 15), ("Etiqueta C", 40), ("Etiqueta D", 10), ("Etiqueta E", 20)]
dibujar_grafico_torta(datos)