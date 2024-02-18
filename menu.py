from nodo import Student, Lista

doubly_linked_list = Lista()
option = 0

while(option != 5):
    print('Lista doblemente enlazada')
    print('1. Agregar al inicio')
    print('2. Agregar al final')
    print('3. Eliminar por valor')
    print('4. Mostrar lista')
    print('5. Salir')
    option = int(input('Ingrese una opción: '))

    if option == 1:
        name = input('Ingrese el nombre del estudiante: ')
        last_name = input('Ingrese el apellido del estudiante: ')
        student_card = input('Ingrese el número de carnet: ')
        data = Student(name, last_name, student_card)
        doubly_linked_list.addStart(data)
        input('Presione enter para continuar')
    if option == 2:
        name = input('Ingrese el nombre del estudiante: ')
        last_name = input('Ingrese el apellido del estudiante: ')
        student_card = input('Ingrese el número de carnet: ')
        data = Student(name, last_name, student_card)
        doubly_linked_list.addEnd(data)
        input('Presione enter para continuar')
    elif option == 3:
        doubly_linked_list.delete()
        input('Presione enter para continuar')
    elif option == 4:
        doubly_linked_list.getAll()
        input('Presione enter para continuar')
    else:
        print('Sesión finalizada')
