from math import sqrt

A = int(input("ingresa el valor de A :"))

B = int(input("ingresa el valor de B :"))

C = int(input("ingresa el valor de C :"))

x1 = 0

x2 = 0

if ((B**2) - (4*A*C)) < 0:
    print("no se puede realizar porque no se puede sacar raiz a un numero negativo")
else:
    x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)  
    x2 = (-B - sqrt ((B**2)-(4*A*C)))/(2*A)

    print("La solucion es: \n x1=",x1, "\n x2=",x2)





