

for Registro in range(101):

    if Registro <= 100:
        Nombre = input('Escribe tu nombre: ')
        Correo = input(' Cual es tu Email: ')
        print('Gracias por Registrarte ')
        Registro += 1
        print('Tu numero de regisrtro es: {}'.format(Registro))

    else:
        print('Lo sentimos, el registro ha terminado.')
