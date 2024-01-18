palabra1=input("ingresa palabra uno: ")
palabra2=input("ingresa segunda palabra: ")

if len(palabra1) < 3 or len(palabra2) < 3:
    print ("no pueden rimar")
elif palabra1[-3 : ] == palabra2[-3 : ]:
    print (" si riman")    
elif palabra1[-2 : ] == palabra2 [-2 : ]:
    print("si riman")
else:
    print (" no  riman")