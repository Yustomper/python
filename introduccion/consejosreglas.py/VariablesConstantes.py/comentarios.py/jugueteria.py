"""class persona():
    def __init__(self,nombre,edad,DNI):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
    def presentarse(self):
        print("hola soy",self.nombre," y mi edad es ",self.edad)

Persona=persona("sebastian",1,000000)
Persona.presentarse()

class trabajador(persona):
    def __init__ (self,nombre,edad,DNI,sueldo,direccion):
        super().__init__(nombre,edad,DNI)
        self.sueldo=sueldo
        self.direccion=direccion
    def sueldoanual(self):
        self.sueldoanual=self.sueldo*12
        print (self.sueldoanual)

class estudiante(persona):
    def __init__(self,nombre,edad,DNI,universidad,calificacion):
        super().__init__(nombre,edad,DNI)
        self.universidad=universidad
        self.calificacion=calificacion

    def presentarEstudiante(self):
        print("me llamo ",self.nombre,"y mi calificacion es :",self.calificacion)

Trabajador=trabajador("francisco",30,111111,1500,"bosnia 7438")
Trabajador.presentarse()
print (Trabajador.DNI)
print(Trabajador.direccion)
Trabajador.sueldoanual()
Estudiante=estudiante("francisco",30,111111,"inacap",7.0)
Estudiante.presentarEstudiante()"""

"""class estudiante():
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def calcular(self):
        if self.nota <5:
            print("reprobado")
        else:
            print("aprobado")
class sebastian(estudiante):
    pass

Estudiante=estudiante("francisco",7)
Estudiante.calcular()
Sebastian=sebastian("sebastian",7)
Sebastian.calcular()"""

"""class calculadora():
    def __init__(self):
        self.n1=int(input("n1"))
        self.n2=int(input("n2"))
    def sumar(self):
        self.sumar=self.n1+self.n2
        print(self.sumar)

imprimir=calculadora()
imprimir.sumar()"""

class Fabrica():
    def __init__(self,color,precio,ruedas):
        self.color=color
        self.precio=precio
        self.ruedas=ruedas
    def presentar(self):
        print("soy un carro de color",self.color,"y tengo :",self.ruedas,"ruedas")

class Auto(Fabrica):  
    pass

class Autobus(Fabrica):
        pass
  

auto=Auto("Rojo",1500,5) 
auto.presentar()
autobus=Autobus("azul",5000,8)
autobus.presentar()


