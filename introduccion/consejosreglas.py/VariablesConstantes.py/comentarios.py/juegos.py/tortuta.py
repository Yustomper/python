import turtle
import random


s = turtle.Screen()
s.title("Tortuguita")
s.bgcolor("gray")

jugador1=turtle.Turtle()#crea un puntero
jugador2=turtle.Turtle()#crea segundo jugador



"""creando jugadores"""
jugador1.hideturtle()
jugador1.shape("turtle")#forma de tortuga
jugador1.color("green")# color de la tortuga
jugador1.shapesize(2,2,2)#tamaño de tortuga
jugador1.pensize(3)#tamaño de lineas

jugador2.hideturtle()
jugador2.shape("turtle")#forma jugador 2
jugador2.color("blue")#color jugador 2
jugador2.shapesize(2,2,2)#tamaño de tortuga
jugador2.pensize(3)#tamaño de linea

"""creando metas"""

jugador1.penup()# esto hace que la caminar la tortuga, no dibuje sobre el camino
jugador1.goto(200,200)#cordenadas donde estarà tortuga
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-250,225)
jugador1.showturtle()



jugador2.penup()# esto hace que la caminar la tortuga, no dibuje sobre el camino
jugador2.goto(200,-200)#cordenadas donde estarà tortuga
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-250,-170)
jugador2.showturtle()


dado=[1,2,3,4,5,6]

for i in range(20):
    if jugador1.pos()>=(200,200):
        print ("la tortuga verde gano")
        break
    elif jugador2.pos() >= (200,-200):
        print("la tortuga azul gana")
        break
    else:
        turno1=input("presione la tecla enter para avanzar :")
        turno1=random.choice(dado)
        print("tu numero es :",turno1,"avanzas",turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2=input("presiona la tecla enter para avanzar  :")
        turno2=random.choice(dado)
        print("tu numero 2 :",turno2 ,"has avanzado :",turno2*20)
        jugador2.pendown()
        jugador2.forward(turno2*20)


jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-250,-170)
jugador2.showturtle()


turtle.done()#mantiene ventana abierta
