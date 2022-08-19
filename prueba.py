frase = 'Hello World!'
lista = frase.split(' ')
print()
print(lista)
print()
#Comentario de Paula
match frase:
    case 'Hello, World!':
        print('Welcome to my home!')
        
    case 'Goodbye, World!':
        print('See you later')
    case _:
         print('No match found')
         
print()

