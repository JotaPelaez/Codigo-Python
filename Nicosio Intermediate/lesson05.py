#TODO REGULAR EXPRESSIONS. Las expresiones regulares se usan para filtrar cadenas o textos. La sintáxis de las RE es la misma en diferentes lenguajes de programación. En Python necesitamos importar RE para trabajar con expresiones regulares
import re

#TODO Search nos sirve para saber si una cadena ocurre dentro de otra.
# r=re.search('si', 'Me gusta la pizza si tiene mucho queso')
# print()
# print(r) #---> La respuesta es   <re.Match object; span=(18, 20), match='si'>

# #Cambiamos la ubicacón del 'si
# r=re.search('si', 'Me gusta la pizza tiene mucho quesi')
# print(r) #---> La respuesta es   <re.Match object; span=(33, 35), match='si'>

# #Cambiamos a mayúsculas el 'SI
# r=re.search('si', 'Me gusta la pizza tiene mucho queSIto')
# print(r) #---> La respuesta es   None
# print()

#TODO Podemos cambiar las respuestas de match 'si' y None a un resultado booleano, agregando al final una comparación. Ojo overmatching y undermatching
# r=re.search('si', 'Me gusta la pizza si tiene mucho queso')!=None
# print(r) #---> La respuesta es   True

# #Cambiamos la ubicacón del 'si
# r=re.search('si', 'Me gusta la pizza tiene mucho quesi')!=None
# print(r) #---> La respuesta es   True

# #Cambiamos a mayúsculas el 'SI
# r=re.search('si', 'Me gusta la pizza tiene mucho queSIto')!=None
# print(r) #---> La respuesta es   False
# print()

#TODO Podemos utilizar el metacaracter de punto. Son caracteres que dan indicaciones especiales sobre un funcionamiento en particular. El punto significa cualquier caracter.
# m=re.search(r'.er ', 'Me gusta comer la pizza')!=None
# print(m) #---> La respuesta es   True

#Terminacion en 'er' mas un espacio y precedido de cualquier caracter
# m=re.search(r'.er ', 'Me gusta ser programador')!=None
# print(m) #---> La respuesta es   True

# #Terminacion en 'er' mas un espacio y precedido de cualquier caracter
# m=re.search(r'.er ', 'Me gusta lavar el auto')!=None
# print(m) #---> La respuesta es   False
# print()

# #Palabras de tres letras que acaban con 'er'
# m=re.search(r' .er ', 'Me gusta comer la pizza')!=None
# print(m) #---> La respuesta es   False
# m=re.search(r' .er ', 'Me gusta ser programador')!=None
# print(m) #---> La respuesta es   True
# print()

#TODO Cuando deseamos crear una busqueda en la cual determinada posicion de caracter pueda tener varias opciones, podemos hacer uso de las 'clases de caracteres' empleando los corchetes []
# l=re.search(r' pas[aeo] ', 'Algo pasa en el estadio')!=None
# print()
# print(l) #---> La respuesta es   True

# #Palabra sola 'pasa','pase' o 'paso'
# l=re.search(r' pas[aeo] ', 'El jugador hizo un pase espaecial')!=None
# print(l) #---> La respuesta es   True

# #Palabra sola 'pasa','pase' o 'paso'
# l=re.search(r' pas[aeo] ', 'Al final nadie paso del grupo')!=None
# print(l) #---> La respuesta es   True

# #Palabra sola 'pasa','pase' o 'paso'
# l=re.search(r' pas[aeo] ', 'Me gusta comer pizza')!=None
# print(l) #---> La respuesta es   False
# print()

#TODO Se pueden poner rangos en lugar de escribir todos los caracteres.Por ejemplo [a-e] indica las letras que van desde a hasta la e = [abcde] o el rango [0-5] indica los numeros que van desde 0 hasta el 5 = [012345] 
# l=re.search(r' 1[0-9] ', 'El costo es de 15 pesos')!=None
# print()
# print(l) #---> La respuesta es   True

# #Numero solo '10','11','12','13','14','15','16','17','18' o '19'
# l=re.search(r' 1[0-9] ', 'El costo es de 5 pesos')!=None
# print(l) #---> La respuesta es   False
# print()

#TODO Se puede realizar la busqueda indicando cualquier cantidad de caracteres con el '*' asterisco, antes o despues del rango
l=re.search(r' *[0-9]', 'El costo es de 5 pesos')!=None
print()
print(l) #---> La respuesta es   True

l=re.search(r' *[0-9]*', 'El codigo es abc1d')!=None
print(l) #---> La respuesta es   True

l=re.search(r' *[0-9]', 'El password es abc')!=None
print(l) #---> La respuesta es   False
print()

#TODO Ver video 18/33 by Nicosio. Uso de 'complemento', 'match', '$', '?' y 'cuantificador{2}' 

#TODO Ver video 19/33 by Nicosio. Uso de 'findall', 'alteraciones', 'split', y 'sub'