from turtle import Turtle, Screen
from itertools import cycle


def dibujar_torta(pincel, radio, datos):
    """Esta función se encarga de dibujar la torta. Recibe un pincel(Turtle), el radio del circulo y
    los datos a dibujar."""

    colores = cycle(
        ["#CB0C14", "#CB6F42", "#83A541", "#6CCB62", "#6596CB", "#815BCB", "#CB3EB7", "#2EC8CB",
         "#2345CB"])

    pincel.pensize(3)
    pincel.pencolor("white")
    pincel.penup()
    pincel.sety(-radio)
    pincel.pendown()

    total = sum(fraccion for _, fraccion in datos)  # data doesn't sum to 100 so adjust

    for _, fraction in datos:
        color = next(colores)
        pincel.fillcolor(color)
        pincel.begin_fill()
        pincel.circle(radio, fraction * 360 / total)
        posicion = pincel.position()
        pincel.goto(0, 0)
        pincel.end_fill()
        pincel.setposition(posicion)


# The labels

def dibujar_etiquetas(pincel, radio, datos):
    """Esta función se encarga de dibujar las etiquetas para cada porción de la torta.
    Recibe un pincel(Turtle), el radio del circulo, los datos y un total"""

    total = sum(fraccion for _, fraccion in datos)  # data doesn't sum to 100 so adjust

    radio_etiqueta = radio * 1.33
    tamaño_fuente = 18
    fuente = ("Ariel", tamaño_fuente, "bold")

    pincel.penup()
    pincel.sety(-radio_etiqueta)

    for label, fraction in datos:
        pincel.circle(radio_etiqueta, fraction * 360 / total / 2)
        pincel.write(label, align="center", font=fuente)
        pincel.circle(radio_etiqueta, fraction * 360 / total / 2)

    screen = Screen()
    screen.exitonclick()


def dibujar(datos, radio=200):
    """Esta función recibe en datos una lista de tuplas, donde cada tupla tiene una etiquta y un valor a graficar en
     la torta. El radio por defecto es 200"""

    pincel = Turtle()
    pincel.speed(10)

    dibujar_torta(pincel, radio, datos)
    pincel.pencolor("black")
    dibujar_etiquetas(pincel, radio, datos)


porcentaje = [("Etiqueta A", 20), ("Etiqueta B", 200), ("Etiqueta C", 20), ("Etiqueta D", 20), ("Etiqueta E", 1)]
dibujar(porcentaje)
