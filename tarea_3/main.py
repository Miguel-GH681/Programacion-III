from arbol_binario import ArbolBinario

arbol_binario = ArbolBinario()
opcion = 0

while(opcion != 6):
    print('Menú principal')
    print('1. Leer documento ')
    print('2. Insertar dato ')
    print('3. Buscar dato ')
    print('4. Eliminar dato')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        try:
            valor = input('Ingrese la ubicación de su archivo: ')
            with open(valor, 'r') as archivo:
                for linea in archivo:
                    arbol_binario.insert(int(linea.strip()))
            print('El recorrido inorden del nuevo árbol creado queda de la siguiente manera: ')
            arbol_binario.inorden()
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 2:
        try:
            valor = int(input('Ingrese un nuevo valor: '))
            arbol_binario.insert(valor)
            print('El recorrido inorden del nuevo árbol creado queda de la siguiente manera: ')
            arbol_binario.inorden()
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 3:
        try:
            valor = int(input('Ingrese el valor que desea buscar: '))
            print(arbol_binario.buscar(valor))
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 4:
        try:
            valor = int(input('Ingrese el valor que desea eliminar: '))
            arbol_binario.eliminar(valor)
            print('El recorrido inorden del nuevo árbol creado queda de la siguiente manera: ')
            arbol_binario.inorden()
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    else:
        print('Ingrese una opción válida')
        input('Presione enter para continuar')

