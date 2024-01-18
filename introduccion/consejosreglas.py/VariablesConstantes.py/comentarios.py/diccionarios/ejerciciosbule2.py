num1=int(input("ingrese 1 numero :"))
num2=int(input("ingrese el segundo numero :"))

for i in range(num1,num2+1):
    if i % 2 == 0:
        continue
    print (i)