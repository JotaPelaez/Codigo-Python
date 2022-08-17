# #TODO Video 4/33 Nicosio. Leemos un archivo de texto linea por linea. Abrimos el archivo para lectura.
# archivo = open('miTexto.txt','r')
# print()
# #TODO Recorremos el archivo linea por linea
# for linea in archivo:
#     print(linea.rstrip())
# print()
# #TODO Si necesitamos saber si el archivo esta cerrado
# cerrado = archivo.closed
# print("El archivo esta cerrado", cerrado)

# #TODO Cerramos el archivo
# archivo.close()
# # Esto es una comprobacion de que el archivo fue cerrado
# cerrado = archivo.closed
# print("El archivo esta cerrado", cerrado)
# print()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#TODO Podemos abrir el archivo y guardarlo en una lista. Cada linea es un elemento de la lista
lista = open('miTexto.txt').readlines()
#Imprimimos la lista
print(lista)
print()
#TODO Recorremos la lista linea por linea
for linea in lista:
    #Imprimimos linea x linea
    print(linea)
print()
lista.close()