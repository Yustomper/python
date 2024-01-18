jugadores = {1:"casillas",3:"pique",15:"ramos"}
print("ingresa un numero para decir el apellido del futbolista :")
numero = int(input("ingresa el numero: "))
if numero in jugadores:
    print (jugadores[numero])
else:
    print("no se encuentra ese jugador")    