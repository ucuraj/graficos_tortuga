from turtle import Turtle, Screen
from itertools import cycle
from random import shuffle


def _dibujar_torta(pincel, radio, datos):
    """Esta función se encarga de dibujar la torta. Recibe un pincel(Turtle), el radio del circulo y
    los datos a dibujar."""

    colores = ["#8251FA", "#FA60C8", "#FA5262", "#FAA039", "#FAF40C", "#A4FA72", "#74FABC", "#77B8FA", "#4F5EFA",
               "#FA1D38"]

    shuffle(colores)
    ciclo_colores = cycle(colores)  # colores en rgb.

    pincel.penup()
    pincel.sety(-radio)
    pincel.pendown()

    total = sum(fraccion for _, fraccion in datos)  # data doesn't sum to 100 so adjust

    for _, fraccion in datos:  # _, ignora etiqueta al desempaquetar los datos de la tupla.
        color = next(ciclo_colores)
        pincel.pencolor(color)
        pincel.fillcolor(color)
        pincel.begin_fill()
        pincel.circle(radio, fraccion * 360 / total)
        posicion = pincel.position()
        pincel.goto(0, 0)
        pincel.end_fill()
        pincel.setposition(posicion)


def _dibujar_etiquetas(pincel, radio, datos):
    """Esta función se encarga de dibujar las etiquetas para cada porción de la torta.
    Recibe un pincel(Turtle), el radio del circulo, los datos y un total"""

    total = sum(fraccion for _, fraccion in datos)  # data doesn't sum to 100 so adjust

    radio_etiqueta = radio * 1.33
    tamaño_fuente = 18
    fuente = ("Ariel", tamaño_fuente, "bold")

    pincel.penup()
    pincel.sety(-radio_etiqueta)

    for etiqueta, fraccion in datos:
        pincel.circle(radio_etiqueta, fraccion * 360 / total / 2)
        pincel.write(etiqueta, align="center", font=fuente)
        pincel.circle(radio_etiqueta, fraccion * 360 / total / 2)


def dibujar_grafico_torta(datos, radio=200):
    """Esta función recibe en datos una lista de tuplas, donde cada tupla tiene una etiquta y un valor a graficar en
     la torta. El radio por defecto es 200"""
    pincel = Turtle()
    pincel.speed(10)
    ventana = Screen()
    _dibujar_torta(pincel, radio, datos)
    pincel.pencolor("black")
    _dibujar_etiquetas(pincel, radio, datos)
    ventana.exitonclick()
