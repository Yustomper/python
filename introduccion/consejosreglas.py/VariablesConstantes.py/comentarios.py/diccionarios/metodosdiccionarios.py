diccionario = {1:2,2:3,3:4}
diccionario2 ={4:6,6:7}
diccionario[5]=6
print(diccionario)
diccionario.pop(3)
print(diccionario)
print(diccionario.get(5))
diccionario.setdefault(7,8)
print(diccionario)
diccionario.update(diccionario2)
print(diccionario)