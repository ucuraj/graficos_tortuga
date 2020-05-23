import turtle

def dibujar_grafico_barras(datos, color="red"):
    """Esta función se encarga de cargar los datos y llamar a la función configurar con los y el color de relleno.
    Recibe una lista con los datos a graficar y un color de relleno, por defecto rojo"""
    valores_x = []
    valores_y = []
    lista_de_datos = []

    for i in range(len(datos)):
        valores_x.append(str((i + 1) * 10))
        valores_y.append(str((i + 1) * 10))
    for i in datos:
        lista_de_datos.append(str(i * 10))

    ventana = turtle.Screen()
    configurar(valores_x, valores_y, lista_de_datos, color)
    ventana.exitonclick()


def configurar(valores_x, valores_y, lista_de_datos, color):
    """Esta función configura las tortugas y luego dibuja. Recibe una lista con los valores del eje X, una lista con
    los valores del eje Y, y una lista con los valores de los datos a dibujar."""

    turtle.setup(width=.85, height=.75)  # configura el ancho y largo de la ventana con valores porcentuales.

    # Definir pinceles
    tortuga_en_X = turtle.Pen()
    tortuga_en_X.speed(0)
    tortuga_en_Y = turtle.Pen()
    tortuga_en_Y.speed(0)
    tortuga_graficar = turtle.Pen()
    tortuga_graficar_lineasPunteadas = turtle.Pen()
    tortuga_etiqueta = turtle.Pen()
    tortuga_etiqueta.speed(0)

    # Ocultar tortuga
    tortuga_graficar.hideturtle()
    tortuga_graficar_lineasPunteadas.hideturtle()
    tortuga_etiqueta.hideturtle()

    # Levantar pincel
    tortuga_en_X.up()
    tortuga_en_Y.up()
    tortuga_graficar.up()
    tortuga_graficar_lineasPunteadas.up()
    tortuga_etiqueta.up()
    10

    # Posicionar tortuga
    tortuga_en_X.setpos(-500, -250)
    tortuga_en_Y.setpos(-500, -250)
    tortuga_graficar.setpos(-500, -250)
    tortuga_graficar_lineasPunteadas.setpos(-500, -250)

    # Colocar etiquetas
    etiquetas(tortuga_etiqueta)

    # Dibujar eje x
    eje_x(tortuga_en_X, valores_x)

    # Dibujar eje y
    eje_y(tortuga_en_Y, valores_y)

    # Graficar barras
    tortuga_graficar.color(color)  # indico el color con el que quiero graficar
    graficar(tortuga_graficar, lista_de_datos)

    # Graficar lineas punteadas
    # graficar_lineas(tortuga_graficar_lineasPunteadas)


def etiquetas(tortuga_etiqueta):
    """Esta función se encarga de escribir las etiquetas 'Grafico de barras', 'Eje x', y 'Eje y' en pantalla"""

    titulo = "Gráfico de barras"
    margenXY = 30
    tipografia = "Times New Roman"
    nombre_eje_x = "Eje x"
    nombre_eje_y = "Eje y"

    tortuga_etiqueta.sety(-250 + 500 + 70)
    tortuga_etiqueta.write(titulo, False, align="center", font=(tipografia, 25, "normal"))
    tortuga_etiqueta.sety(-250 - 20 - margenXY - 30)
    tortuga_etiqueta.write(nombre_eje_x, False, align="center", font=(tipografia, 12, "normal"))
    tortuga_etiqueta.setpos(-500, 250 + 60)
    tortuga_etiqueta.write(nombre_eje_y, False, align="center", font=(tipografia, 12, "normal"))


def eje_x(tortuga_en_X, valores_x):
    """Esta función se encarga de graficar en pantalla la escala del eje x . Por defecto el largo es: 10"""

    tipografia = "Times New Roman"
    margenXY = 30

    tortuga_en_X.down()
    for valor_x in valores_x:
        tortuga_en_X.forward(100)
        tortuga_en_X.right(90)
        tortuga_en_X.forward(20)
        tortuga_en_X.up()
        tortuga_en_X.forward(margenXY)
        tortuga_en_X.write(valor_x, False, align="center", font=(tipografia, 10, "normal"))
        tortuga_en_X.right(180)
        tortuga_en_X.forward(20 + margenXY)
        tortuga_en_X.down()
        tortuga_en_X.right(90)
    tortuga_en_X.forward(50)


def eje_y(tortuga_en_Y, valores_y):
    """Esta función se encarga de graficar en pantalla la escala del eje y."""

    posicion = -10
    tipografia = "Times New Roman"
    margenXY = 30

    tortuga_en_Y.up()
    tortuga_en_Y.setpos(-500 + posicion, -300 + posicion)
    tortuga_en_Y.write("0", True, align="center",
                       font=(tipografia, 10, "normal"))  # Escribo 0 al principio de la escala de y.
    tortuga_en_Y.setpos(-500, -300)
    tortuga_en_Y.down()
    tortuga_en_Y.left(90)

    for valor_y in valores_y:
        tortuga_en_Y.forward(100)
        tortuga_en_Y.left(90)
        tortuga_en_Y.forward(20)
        tortuga_en_Y.up()
        tortuga_en_Y.forward(margenXY)
        tortuga_en_Y.write(valor_y, False, align="center", font=(tipografia, 10, "normal"))
        tortuga_en_Y.left(180)
        tortuga_en_Y.forward(20 + margenXY)
        tortuga_en_Y.down()
        tortuga_en_Y.left(90)
    tortuga_en_Y.forward(50)


def graficar(tortuga_graficar, lista_de_datos):
    """Esta función grafica los valores recibidos en lista_datos.
    Recibe una tortuga, que es la que va a graficar y la lista de datos"""

    ancho_barra = 40
    tortuga_graficar.forward(100 - ancho_barra / 2)

    for dato in lista_de_datos:
        tortuga_graficar.begin_fill()
        tortuga_graficar.left(90)
        tortuga_graficar.down()
        tortuga_graficar.forward(int(dato) - 50)
        tortuga_graficar.right(90)
        tortuga_graficar.forward(ancho_barra)
        tortuga_graficar.right(90)
        tortuga_graficar.forward(int(dato) - 50)
        tortuga_graficar.left(90)
        tortuga_graficar.up()
        tortuga_graficar.forward(100 - ancho_barra)
        tortuga_graficar.end_fill()


def graficar_lineas(tortuga_graficar_lineasPunteadas):
    for i in range(5):
        tortuga_graficar_lineasPunteadas.setpos(-500, -250 + 100 * (i + 1))

        for j in range(105):
            tortuga_graficar_lineasPunteadas.down()
            tortuga_graficar_lineasPunteadas.forward(5)
            tortuga_graficar_lineasPunteadas.up()
            tortuga_graficar_lineasPunteadas.forward(5)
