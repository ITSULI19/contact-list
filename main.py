#agenda de contactos

#funcion agregar contactos
def agregar_contacto(agenda):
    print('agregar contacto')
    nombre = str(input('ingrese el nombre del contacto: '))
    telefono = int(input('ingrese el numero telefonico: '))
    email = input('ingrese su email: ')

    agenda[nombre] = {'telefono':telefono, 'email': email}
    print(f'contacto: {nombre} fue guardado')

#funcion eliminar contactos
def eliminar_contacto(agenda):
    print('eliminar contacto')
    nombre = input('escriba el nombre del contacto que desea borrar: ')
    if agenda.pop(nombre):
        print(f'contacto {nombre} borrado')
    else:
        print('contacto no encontrado')

#funcion buscar contactos
def buscar_contacto(agenda):
    print('buscar contacto')
    nombre = input('ingrese el nombre del contacto que desea buscar: ')
    contacto = agenda.get(nombre)
    if contacto:
        print(f"{nombre} - telefono {contacto['telefono']}, email: {contacto['email']}")
    else:
        print('contacto no encontrado')

#funcion mostrar todos los contactos
def mostrar_contactos(agenda):
    if not agenda:
        print('la agenda esta vacia')
        return
    for nombre in sorted(agenda):
        contacto = agenda[nombre]
        print(f"{nombre} - telefono: {contacto['telefono']}, email:{contacto['email']}")


#diccionario
agenda = {}

#menu
while True:
    print('\n1. agregar contacto')
    print('2. eliminar contacto')
    print('3. buscar contacto')
    print('4. mostrar todos los contactos')
    print('5. salir')
    #opcion
    opcion = input('escoje una opcion de las anteriores: ')

    if opcion == '1':
        agregar_contacto(agenda)
    elif opcion == '2':
        eliminar_contacto(agenda)
    elif opcion == '3':
        buscar_contacto(agenda)
    elif opcion == '4':
        mostrar_contactos(agenda)
    elif opcion == '5':
        print('saliendo de la agenda')
        break
    else:
        print('opcion invalida')
