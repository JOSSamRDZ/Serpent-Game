import turtle
import time  # Usamos el módulo time para ralentizar la velocidad de nuestro elemento
import random  # para manejar la aparición de la comida
# Intervalo de pausa entre movimientos
posponer = 0.1

# Configuración de la ventana
window = turtle.Screen()
window.title("Serpent Game")
window.bgcolor("gray")
window.setup(width=600, height=600)
# Desactiva actualizaciones automáticas para mejorar las animaciones
window.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()  # Evita que la serpiente deje un rastro al moverse
cabeza.goto(0, 0)  # Establece la posición inicial de la serpiente
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 0)
# Segmentos / cuerpo de la serpiente
# Usamos una lista para agregarle cuerpo a la serpiente cada vez que coma una fruta
segmento = []


# Funciones para cambiar la dirección de la serpiente
def arriba():
    if cabeza.direction != "down":  # Evita que la serpiente se mueva en dirección opuesta
        cabeza.direction = "up"


def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"


def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"


def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"

# Función para mover la serpiente


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()  # Obtiene la coordenada Y actual de la serpiente
        cabeza.sety(y + 10)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 10)
    if cabeza.direction == "left":
        x = cabeza.xcor()  # Obtiene la coordenada X actual de la serpiente
        cabeza.setx(x - 10)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 10)


# Configuración del teclado
window.listen()  # Funcion que nos permite escuchar las teclas de laws flechas del teclado
window.onkeypress(arriba, "Up")
window.onkeypress(abajo, "Down")
window.onkeypress(izquierda, "Left")
window.onkeypress(derecha, "Right")

# Bucle principal del juego
while True:
    window.update()  # Actualiza la ventana
    # 20 por que si la distancia entre los dos objetos es igual a sus medidas significa que se han tocado
    if cabeza.distance(comida) < 20:
        # el margen es igual a casi el tamaño de la cuadricula
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)
        # Aqui cambiamos los atributos del elemento cada vez que come una manzana
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("black")
        nuevo_segmento.penup()
        segmento.append(nuevo_segmento)
    #mover el cuerpo de la serpiente
    totalSeg= len(segmento)
    for index in range(totalSeg - 1,0,-1 ):
        x = segmento[index - 1].xcor()
        y = segmento[index - 1].ycor()
        segmento[index].goto(x,y)
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmento[0].goto(x,y)
    mov()
    # Pausa la ejecución para ralentizar el movimiento de la serpiente
    time.sleep(posponer)

# Mantener la ventana abierta
turtle.done()
