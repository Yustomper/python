from tkinter import *
def sumar():
    variable3.set( float(variable1.get()+float(variable2.get())))

def limpiar():
    variable1.set("")
    variable2.set("")    
    

root=Tk()
root.config(bd=15)
root.config(cursor="heart")

variable1=StringVar()
variable2=StringVar()
variable3=StringVar()

titulo1 = Label(root,text="numero1")
titulo1.pack()
entrada1=Entry(root, justify="center", textvariable=variable1)
entrada1.pack()

titulo2 = Label(root,text="numero2")
titulo2.pack()
entrada2=Entry(root, justify="center", textvariable=variable1)
entrada2.pack()

titulo3 = Label(root,text="resultado")
titulo3.pack()
entrada3=Entry(root, justify="center", textvariable=variable1)
entrada3.pack()

boton = Button(root,text="sumar", command=sumar)
boton.pack()
root.mainloop()