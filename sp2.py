import turtle
#Usamos el modulo time para realentizar la velocidad de nuestro elemento
import time #La función time.sleep(segundos) pausa la ejecución del programa durante el número de segundos especificado.
posponer = 0.1
#Configuración de la ventana
window =  turtle.Screen()
window.title ("Serpent Game")
window.bgcolor("gray")
window.setup(width=600, height=600)
window.tracer(0)#Mejora las animaciones, según...

#Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()#Aunque movamos el elemeno no deja ningun rastro
cabeza.goto(0,0)#Le da una posición al elemento
cabeza.direction = "stop"
# Funciones para cambiar la dirección de la serpiente
def arriba():
    if cabeza.direction != "down":  # Evitar movimiento en dirección opuesta
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

#Funcion mov para el set de movimientos
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor() #Obtiene la cordenada del elemnto
        cabeza.sety(y+10)
    if cabeza.direction == "down":
        y = cabeza.ycor() 
        cabeza.sety(y-10)
    if cabeza.direction == "left":
        x = cabeza.xcor() 
        cabeza.setx(x-10)
    if cabeza.direction == "right":
        x = cabeza.xcor() #Obtiene la cordenada del elemnto
        cabeza.setx(x+10)
        
#Teclado
#Conectamos el teclado, despues de las funciones del control del elemento y direccón
window.listen()
window.onkeypress(arriba,"Up")
window.onkeypress(abajo,"Down")
window.onkeypress(izquierda,"Left")
window.onkeypress(derecha,"Right")
#Crear un bucle principal o while loop
while True:
    window.update() #CUANDO CREAMOS UN JUEGO TEMEMOS QUE TENER UN BULE PRINCIPAL
    mov()
    time.sleep(posponer) #Aquí especificamente realentizamos el tiempo del movimiento de nuestro elemento con la función time.sleep
#Mantener la ventana abierta
turtle.done()