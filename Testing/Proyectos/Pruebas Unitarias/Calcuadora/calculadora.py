'''
Calculadora con las operaciones basicas
las cuales son Sumar, Restar, Multiplicar, Dividir, Potencia

'''

class Calculadora:
    def sumar(self, num1, num2):
        if (type(num1) != str and type(num2) != str):
            if (num1 >= 0 and num2 >= 0):
                if(type(num1) == int and type(num2) == int):
                    return num1 + num2
                else:
                    return 'Solo se puede sumar numeros enteros'
            else:
                return 'Solo se puede sumar numeros positivos y el cero'
        else:
            return 'Solo se pueden sumar numeros'
        
    def restar(self, num1, num2):
        if (type(num1) != str and type(num2) != str):
            if (num1 >= 0 and num2 >= 0):
                if(type(num1) == int and type(num2) == int):
                    return num1 - num2
                else:
                    return 'Solo se puede restar numeros enteros'
            else:
                return 'Solo se puede restar numeros positivos y el cero'
        else:
            return 'Solo se pueden restar numeros'
        

    def multiplicar(self, num1, num2):
        if (type(num1) != str and type(num2) != str):
            if (num1 >= 0 and num2 >= 0):
                if(type(num1) == int and type(num2) == int):
                    return num1 * num2
                else:
                    return 'Solo se puede multiplicar numeros enteros'
            else:
                return 'Solo se puede multiplicar numeros positivos y el cero'
        else:
            return 'Solo se pueden multiplicar numeros'
        

    def dividir(self, num1, num2):
        if (type(num1) != str and type(num2) != str):
            if (num1 > 0 and num2 > 0):
                if(type(num1) == int and type(num2) == int):
                    return num1 / num2
                else:
                    return 'Solo se puede dividir numeros enteros'
            else:
                return 'Solo se puede dividir positivos'
        else:
            return 'Solo se pueden dividir numeros'
        
