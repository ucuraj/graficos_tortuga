import turtle
from grafico_de_torta.grafico_de_torta import dibujar_grafico_torta
from grafico_de_barras.grafico_de_barras import dibujar_grafico_barras


##### Grafico de barras
datos=[20,20,20,20,20]#[20, 30, 60, 20, 10]
etiqueta = ["A","B","C","D","E"]
dibujar_grafico_barras(datos,etiqueta, color="green")

##### Grafico de torta
datos = [("Etiqueta A", 30), ("Etiqueta B", 15), ("Etiqueta C", 40), ("Etiqueta D", 10), ("Etiqueta E", 20)]
dibujar_grafico_torta(datos)

print("presione una click derecho para finalizar")
turtle.exitonclick()