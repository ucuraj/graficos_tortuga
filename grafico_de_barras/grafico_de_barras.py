import turtle
import tkinter
import time

initPosX,initPosY= -300,-250
turtle.clearscreen()

def dibujar_grafico_barras(datos=[], etiquetas=[], color="red",tiempo=3):
    """Esta función se encarga de cargar los datos y llamar a la función configurar con los datos y el color de relleno.
    Recibe una lista con los datos a graficar, las etiquetas y un color de relleno, por defecto rojo
    Los parametros tienen que respetar una estructura como la siguiente:
    
    datos = (lista de enteros) [20,20,20,20,20]
    etiqueta = (lista de cadena de caracteres) ["A","B","C","D","E"]
    color = (cadena de caracteres) = "red" , "green", "yellow", "black", "blue", etc
    para mas informacion sobre todos los colores puede visitar el siguiente link:
    (http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter)
    tiempo = (entero) 1,2,3,4,5 ... N -> representa el tiempo el cual se va a visualizar el grafico antes que pueda eliminarse

    Ejemplo de uso:

    Se tiene que llamar a la funcion con una seleccion de parametros como la siguiente
     
    *solo mandando los valores de los graficos
    dibujar_graficos_barras([20,20,20,20,20])
    
    *mandando los graficos y la etiquetas
    dibujar_graficos_barras([20,20,20,20,20],["A","B","C","D","E"])

    *incorporando un color diferente al rojo
    dibujar_graficos_barras([20,20,20,20,20],["A","B","C","D","E"],"green")
    """

    if len(datos)!=len(etiquetas):
        print("¡¡¡¡¡¡¡ERROR!!!!!!")
        print("""Se ingresaron cantidades diferentes entre los datos y las etiquetas en los parametros del Grafico
          de Barras,por favor revise nuevamente que la cantidad de datos coincida""")
        exit(1)

    turtle.clearscreen()

    turtle.Screen().clear()
    valores_y = []
    lista_de_datos = []

    exponente = obtener_exponente(datos)
    longitud = (max(datos) // (10 ** exponente)) + 1
    
    #Modifico los datos recibidos para que se grafiquen correctamente
    for i in datos:
        lista_de_datos.append(i / (10 ** (exponente-2)))

    #Asigno etiquetas estandar cuando no se recibe ninguna
    if(etiquetas == []):
        for i in range(len(datos)):
            etiquetas.append("Categoria " + str(i+1))

    #Asigno los valores al eje y    
    for i in range(longitud):
        valores_y.append(str((i + 1) * (10 ** exponente)))

    configurar(etiquetas, valores_y, lista_de_datos, color,tiempo)
    

def obtener_exponente(datos):
    """Esta funcion retorna la potencia a la que se eleva el maximo numero recibido en la lista de datos con base 10"""
    maximo = max(datos) #Obtengo el maximo valor de la lista, llamada datos
    
    exponente = 0;
    while (maximo > 10):
        exponente += 1
        maximo = maximo / 10
    return exponente


def configurar(valores_x, valores_y, lista_de_datos, color,tiempo=3):
    """Esta función configura las tortugas y luego dibuja. Recibe una lista con los valores del eje X, una lista con
    los valores del eje Y, y una lista con los valores de los datos a dibujar."""


    turtle.setup(width=.75, height=.85)  #configura el ancho y largo de la ventana.
    screen = turtle.Screen()

    # Definir pinceles
    tortuga_en_X = turtle.Pen()
    tortuga_en_Y = turtle.Pen()
    tortuga_graficar = turtle.Pen()
    tortuga_graficar_lineasPunteadas = turtle.Pen()

    #Aumentar velocidad de la tortuga
    tortuga_en_X.speed(0)
    tortuga_en_Y.speed(0)

    # Ocultar tortuga
    tortuga_graficar.hideturtle()
    tortuga_graficar_lineasPunteadas.hideturtle()

    # Levantar pincel
    tortuga_en_X.up()
    tortuga_en_Y.up()
    tortuga_graficar.up()
    tortuga_graficar_lineasPunteadas.up()

    # Posicionar tortuga
    global initPosX 
    initPosX -= 20*len(lista_de_datos)
    tortuga_en_X.setpos(initPosX, initPosY)
    tortuga_en_Y.setpos(initPosX, initPosY)
    tortuga_graficar.setpos(initPosX, initPosY)
    tortuga_graficar_lineasPunteadas.setpos(initPosX, initPosY)

    # Dibujar eje x
    eje_x(tortuga_en_X, valores_x)

    # Dibujar eje y
    eje_y(tortuga_en_Y, valores_y)

    # Graficar barras
    tortuga_graficar.color(color)  # indico el color con el que quiero graficar
    graficar(tortuga_graficar, lista_de_datos)

    # Graficar lineas punteadas
    #graficar_lineas(tortuga_graficar_lineasPunteadas, valores_x, valores_y)
    
    tkinter.mainloop(30000000)
    time.sleep(tiempo)


def eje_x(tortuga_en_X, valores_x):
    """Esta función se encarga de graficar en pantalla la escala del eje x."""

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
    tortuga_en_Y.setpos(initPosX + posicion, initPosY + posicion)
    tortuga_en_Y.write("0", True, align="center", font=(tipografia, 10, "normal"))
    tortuga_en_Y.setpos(initPosX, initPosY)
    tortuga_en_Y.left(90)
    tortuga_en_Y.down()

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
        tortuga_graficar.forward(int(dato))
        tortuga_graficar.right(90)
        tortuga_graficar.forward(ancho_barra)
        tortuga_graficar.right(90)
        tortuga_graficar.forward(int(dato))
        tortuga_graficar.left(90)
        tortuga_graficar.up()
        tortuga_graficar.forward(100 - ancho_barra)
        tortuga_graficar.end_fill()


def graficar_lineas(tortuga_graficar_lineasPunteadas, valores_x, valores_y):
    for i in range(len(valores_y)):
        tortuga_graficar_lineasPunteadas.setpos(-500, -250 + 100 * (i + 1))

        #Dibujar las lineas punteadas
        for j in range((len(valores_x)+1)*9):
            tortuga_graficar_lineasPunteadas.down()
            tortuga_graficar_lineasPunteadas.forward(5)
            tortuga_graficar_lineasPunteadas.up()
            tortuga_graficar_lineasPunteadas.forward(5)
