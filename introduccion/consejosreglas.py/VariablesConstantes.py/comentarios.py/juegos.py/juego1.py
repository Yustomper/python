import turtle
import time
delay=0.1
wn=turtle.Screen() # crea una ventana

wn.title("Juego Snake")#crea un titulo
wn.setup(width=600,height=600)#dimensiones de la ventana
wn.bgcolor("black")#color de ventana
head=turtle.Turtle()#crea un objeto a partir de turtle
head.speed(0)#vwlocidad de objeto
head.shape("square")#forma de objeto
head.color("green")
head.penup()
head.goto(0,0)
head.direction="up"


def move():
    if head.direction=="up":
        y=head.ycor()
        x=head.ycor()
        head.sety(y+10)

while True:
    wn.update()
    move()    
    time.sleep(delay)    





turtle.done()








turtle.done()

