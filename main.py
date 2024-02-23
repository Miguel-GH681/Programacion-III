from controller import Recursividad

controller = Recursividad()
opcion = 0

while(opcion != 6):
    opcion = int(input("----------Menu principal---------- \n|  1. Convertir a Binario        | \n|  2. Contar Digitos             | \n|  3. Raiz cuadrada Entera       | \n|  4. Convertir decimal desde Romano \n|  5. Suma de numeros enteros    \n|  6. Salir                      | \n----------------------------------\nIngrese una opción: "))

    if opcion == 1:
        try:
            valor = int(input('Ingrese un número para convertirlo a binario: '))
            print(controller.convertir_a_binario(valor))
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 2:
        try:
            valor = int(input('Ingrese un número para obtener el número de dígitos que contiene: '))
            print(controller.contar_digitos(valor))
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 3:
        try:
            valor = int(input('Ingrese un número para obtener su raiz cuadrada entera: '))
            print(controller.raiz_cuadrada_entera(valor))
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 4:
        try:
            valor = input('Ingrese un número romano para convertirlo a decimal: ')
            print(controller.convertir_a_decimal(valor))
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 5:
        try:
            valor = int(input('Ingrese un número para obtener la suma de 0 a dicho número: '))
            print(controller.suma_numeros_enteros(valor))
            input('Presione enter para continuar')
        except:
            print('Ha ocurrido un error, inténtelo nuevamente')
            input('Presione enter para continuar')
    elif opcion == 6:
        print('Sesión finalizada')
    else:
        print('Ingrese una opción válida')
        input('Presione enter para continuar')

