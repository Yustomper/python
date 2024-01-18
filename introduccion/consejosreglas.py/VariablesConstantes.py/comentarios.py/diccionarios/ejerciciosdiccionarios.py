paises = {"Guatemala": "Ciudad de guatemala","Honduras" : "honduras", "Nicaragua":"mangua","costa rica":"sanjose", "panama":"panama"}
print("elige entre guatemala, honduras ,nicaragua , costa rica o panama :")
'''pais1=input("escribe un pais para saber su capital: ")
if pais1 == "guatemala":
    print("la capital es : ",paises.get("guatemala"))
elif pais1 == "honduras":
    print ("la capital es : ",paises.get("honduras"))
elif pais1 =="nicaragua":
    print("la capital es : ",paises.get("nicaragua")) 
elif pais1 == "costa rica":
    print("la capital es : ",paises.get("costa rica"))
elif pais1=="panama":
    print("la capital es : ", paises.get("panama")) 
else:
    print("ese pais no esta en la lista")'''
pais= input("ingresa el pais: ")    
letra = pais.capitalize() in paises

if letra == True:
    print(paises[pais.capitalize()])
else:
    print ("no se encuentra en el diccionario")    