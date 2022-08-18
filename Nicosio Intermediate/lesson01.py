# #TODO Video 3/33 Nicosio. Como crear un archivo de texto. Craemos la cadena que deseamos que se guarde. Prueba en ramaDevop
# cadena = "Es la frase ejemplo para la clase"

# #TODO Escribir archivos. Pasamos el nombre del archivo, si lo deseamos con su ruta e indicamos que es para escrituta
# archivo = open('miArchivo.txt','w')

# #TODO Escribimos al archivo la informacion
# archivo.write(cadena)

# #TODO Cerramos el archivo
# archivo.close()
# print()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

archivo = open('miTexto.txt','w')
n=0

while n<5:
    texto = input("Dame un texto: ")
    archivo.write(texto + '\n')
    n+=1
    
archivo.close
