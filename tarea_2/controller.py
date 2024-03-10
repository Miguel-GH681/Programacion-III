class Recursividad:
    
    def convertir_a_binario(self, numero):
        if numero < 2:
            return str(numero)
        else:
            return self.convertir_a_binario(numero // 2) + str(numero % 2)

    def contar_digitos(self, numero, contador = 1):
        if len(str(numero)) == 0:
            return 'Ingrese un valor válido'
        elif len(str(numero)) == 1:
            return 'La cantidad de dígitos que ingresó es de: ' + str(contador)
        else:
            contador = contador + 1
            return self.contar_digitos(str(numero)[0: (len(str(numero)) - 1)], contador)


    def calcular_raiz_cuadrada(self, num, menor=0, mayor=None):
        if mayor is None:
            mayor = num // 2 + 1

        if menor <= mayor:
            mid = (menor + mayor) // 2
            mid_cuad = mid * mid

            if mid_cuad == num:
                return mid
            elif mid_cuad < num:
                return self.calcular_raiz_cuadrada(num, mid + 1, mayor)
            else:
                return self.calcular_raiz_cuadrada(num, menor, mid - 1)
        else:
            return mayor

    def raiz_cuadrada_entera(self, numero):
        return self.calcular_raiz_cuadrada(numero)

    def convertir_a_decimal(self, numero_romano):
        romano_decimal_list = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if len(numero_romano) == 0:
            return 0

        if len(numero_romano) == 1:
            return romano_decimal_list[numero_romano[0]]

        if romano_decimal_list[numero_romano[0]] < romano_decimal_list[numero_romano[1]]:
            return romano_decimal_list[numero_romano[1]] - romano_decimal_list[numero_romano[0]] + self.convertir_a_decimal(numero_romano[2:])
        else:
            return romano_decimal_list[numero_romano[0]] + self.convertir_a_decimal(numero_romano[1:])
    
    def suma_numeros_enteros(self, numero, contador = 0):
        if numero == 0:
            return 'La suma es de: ' + str(contador);
        else:
            return  self.suma_numeros_enteros(numero -1 ,contador + numero)
