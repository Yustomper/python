#3 candidatos de diferentes colores: A rojo, B verde y C azul
candidatos = input("puedes elegir por el candidato A, el candidato B o el C. Elige tu candidato: ")
if candidatos.upper() =="A":
    print ("elegiste el candidato rojo")
elif candidatos.upper() == "B":
    print ("elegiste el candidato verde")
elif candidatos.upper() =="C":
    print ("elegiste el candidato azul")
else:
    print ("esa letra no es alternativa")        