#TODO Sobrecarga de Operadores.
#Creamos una clase producto, con su constructor(init) y sus correspondientes atributos(nombre y costo) 
class Producto:
    def __init__(self, nombre, costo):
        self.nombre=nombre
        self.costo=costo
    
    #Sobrecarga de string. Para facilitar la impresion y visualizacion de los atributos. Covertir el estado del objeto en una cadena    
    def __str__(self):
        return 'Producto '+self.nombre+' cuesta $'+str(self.costo)    
    
    #Sobrecarga de +. El operando izquierdo esta ejecutando la operacion de suma (self) y el operando derecho es el que va entrar como parametro (p o cualquiera otro)   
    def __add__(self, p):
        #Defino reglas de como sera la concatenacion o suma
        tempN=self.nombre+', '+p.nombre
        tempC=self.costo+p.costo
        return Producto(tempN, tempC) # Realizo la instanciacion de nuevo producto y le paso el nuevo nombre(tempN) y nuevo costo (tempC)
    
    #Sobrecarga de or. En este ejemplo tomamos el mas costoso
    def __or__(self, p):
        #Defino reglas de como sera la comparacion
        if(self.costo>p.costo):
            return Producto(self.nombre, self.costo)
        else:
            return Producto(p.nombre, p.costo)
    
    #Sobrecarga unuario float(solo recibe el self). Lo usaremos para regresar el costo
    def __float__(self):
        return self.costo
    
    #Sobrecarga de +=. Lo usaremos para incrementar el costo
    def __iadd__(self, other):
        self.costo=self.costo + float(other)
        return self
        
    #Sobrecarga de gt (mayor que). Lo usaremos para hacer comparaciones entre productos
    def __gt__(self, other):
        if self.costo > other.costo:
            return True
        else:
            return False    
        
    
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
# Creamos 2 instancias    
manzana = Producto('Manzana roja', 5.6)
pera = Producto('Pera grande', 4.87)

print()
print(manzana)    # la sobrecarga del string, me ayuda a mostrar la informacion
print(pera)     #Sino tuviera la sobrecarga del string, solo me indicaria la referencia a la instancia correspondiente. Algo asi <__main__.Producto object at 0x000001FFE3F9BB80>
print('-------------------------------------')
print()
#Realizo la suma de mis productos
canasta = manzana+pera
print(canasta)
print('-------------------------------------')
print()
#Determino cual es mas costoso
costoso=manzana | pera        #Este es el operador or (|)
print(costoso)
print('-------------------------------------')
print()
#Determino el costo total de 5 manzanas rojas
total=5*float(manzana)
print(total)
print('-------------------------------------')
print()
#Incrementamos el costo de la manzana
manzana+=1.5
print(manzana)
print('-------------------------------------')
print()
#Comparamos productos
if (manzana>pera):
    print("El mas costoso es manzana")
else:
    print("El mas caro es pera")

pera+=10
if (manzana>pera):
    print("El mas costoso es manzana")
else:
    print("El mas caro es pera")

print('-------------------------------------')
print()

#TODO Tipos de Metodos. 1.Metodo de Instancia (video 8-9/33 by Nicosio) utiliza el self como parametro. 2.Metodo de Clase. Utiliza el decorador @classmethod y cls como parametro. 3. Metodo Estatico. Utiliza el decorador @staticmethod y no requiere de parametro.

#TODO Clases internas. Ver video 10/33 by Nicosio