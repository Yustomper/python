'''for i in range(1,11):
    print (i)'''

num1=int(input("ingresa primer numero :"))
num2=int(input("ingresa el segundo numero :"))
if num1>num2:
    print("ingresa en orden de mnor a mayor")
else:
 for i in range(num1,num2+1):
    print(i)