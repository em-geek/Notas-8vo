Característica: Multiplicar dos números
    Como usuario de la calculadora
    Quiero multiplicar dos números
    Para obtener el producto correcto

    Escenario: Multiplicar 3 por 3
        Dado que ingreso el número "3" y el número "3"
        Cuando realizo la operación de multiplicación
        Entonces puedo ver el resultado "9"

    Escenario: Multiplicar 2 por 0
        Dado que ingreso el número "2" y el número "0"
        Cuando realizo la operación de multiplicación
        Entonces puedo ver el resultado "0"

    Escenario: Multiplicar 5 por 1
        Dado que ingreso el número "5" y el número "1"
        Cuando realizo la operación de multiplicación
        Entonces puedo ver el resultado "5"

    Escenario: Multiplicar número negativo y número
        Dado que ingreso el número "-1" y el número "2"
        Cuando realizo la operación de multiplicación
        Entonces puedo ver el mensaje "Solo se puede multiplicar numeros positivos y el cero"

    Escenario: Multiplicar número flotante y número
        Dado que ingreso el flotante "3.5" y el número "2"
        Cuando realizo la operación de multiplicación
        Entonces puedo ver el mensaje "Solo se puede multiplicar numeros enteros"

    Escenario: Multiplicar caracter y número
        Dado que ingreso el caracter "X" y el número "2"
        Cuando realizo la operación de multiplicación
        Entonces puedo ver el mensaje "Solo se pueden multiplicar numeros"

    Escenario: Multiplicar 1 por 1000
        Dado que ingreso el número "1" y el número "1000"
        Cuando realizo la operación de multiplicación
        Entonces puedo ver el resultado "1000"

    Escenario: Multiplicar 100 por 100
        Dado que ingreso el número "100" y el número "100"
        Cuando realizo la operación de multiplicación
        Entonces puedo ver el resultado "10000"

    Escenario: Multiplicar 0 por un número grande
        Dado que ingreso el número "0" y el número "999"
        Cuando realizo la operación de multiplicación
        Entonces puedo ver el resultado "0"