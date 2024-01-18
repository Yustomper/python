def numeros():
    num1=float(input("ingrese el primer numero :"))
    num2=float(input("ingresa el segundo numero :"))
    if num1 > num2:
        return 1
    elif num1<num2:
        return -1
    else:
        return 0
    
print(numeros())    