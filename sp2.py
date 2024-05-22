import turtle
#Configuración de la ventana
window =  turtle.Screen()
window.title ("Serpent Game")
window.bgcolor("gray")
window.setup(width=600, height=600)
window.tracer()

#Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "up"

#Funciones
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+2)


#Crear un bucle principal o while loop
while True:
    window.update()
    mov()
#Mantener la ventana abierta
turtle.done()