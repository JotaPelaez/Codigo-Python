#TODO Propiedades, Getter y Setter.

class Alumno:
    def __init__(self,nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        
#TODO Ahora creamos un GETTER. Creamos un método que funcionará como una propiedad, gracias al decorador "@property". Es un método que nos facilita la impresión de algún estado de los atributos de la clase. Se parece a una sobrecarga de string

    @property
    def nombreLista(self):
        return self.apellido+' '+self.nombre
    
#TODO Ahora creamos un SETTER. Creamos otro método con la propiedad "@nombredeseado.setter" que nos permite usarlo como un setter. Se utiliza para pasar otros datos de atributos.
    @nombreLista.setter
    def nombreLista(self, nombreCompleto):
        self.nombre, self.apellido = nombreCompleto.split(' ')

#TODO Ahora creamos un DELETER. Sirve cuando deseamos eliminar el contenido de un atributo. No lleva parámetros mas allá de self.
    @nombreLista.deleter
    def nombreLista(self):
        #Limpiamos los atributos
        print("Borrando")
        self.nombre=None
        self.apellido=None
    
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#Creamos una instancia
alumno1 = Alumno('José', 'Peláez')

#Ahora usamos la propiedad 'nombreLista'(osea el GETTER) y nos da un valor de salida. 
print()
print(alumno1.nombreLista)

#Ahora asignamos un nuevo valor(osea el SETTER).Es como un input y luego volvemos a confirmar usando de nuevo el getter
alumno1.nombreLista = 'Paula Fernández'    #-----> SETTER
print(alumno1.nombreLista)                 #-----> GETTER
print()

#Ahora borramos el atributo, invocando el deleter
del(alumno1.nombreLista)      

#Ahora el objeto ya no tiene contenidos en los atributos y arrojara una excepcion
# print(alumno1.nombreLista)    #-----> TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
print()