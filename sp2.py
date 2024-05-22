import turtle
import time  # Usamos el módulo time para ralentizar la velocidad de nuestro elemento

# Intervalo de pausa entre movimientos
posponer = 0.1

# Configuración de la ventana
window = turtle.Screen()
window.title("Serpent Game")
window.bgcolor("gray")
window.setup(width=600, height=600)
window.tracer(0)  # Desactiva actualizaciones automáticas para mejorar las animaciones

# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()  # Evita que la serpiente deje un rastro al moverse
cabeza.goto(0, 0)  # Establece la posición inicial de la serpiente
cabeza.direction = "stop"

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
window.listen()
window.onkeypress(arriba, "Up")
window.onkeypress(abajo, "Down")
window.onkeypress(izquierda, "Left")
window.onkeypress(derecha, "Right")

# Bucle principal del juego
while True:
    window.update()  # Actualiza la ventana
    mov()
    time.sleep(posponer)  # Pausa la ejecución para ralentizar el movimiento de la serpiente

# Mantener la ventana abierta
turtle.done()
