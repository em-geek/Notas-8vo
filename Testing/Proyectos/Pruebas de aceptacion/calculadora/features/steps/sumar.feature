Característica: Sumar dos numeros
    Como usuario de la calculadora 
    Deseo sumar dos numeros
    Para tener cálculos precisos

    Escenario: Sumar 2 mas 2
        Dado que ingreso el numero "2" y el numero "2"
        Cuando realizo la operación
        Entonces puedo ver el resultado "4"

    Escenario: Sumar 5 mas 2
        Dado que ingreso el numero "5" y el numero "2"
        Cuando realizo la operación
        Entonces puedo ver el resultado "7"

    Escenario: No acepta caracteres
        Dado que ingreso el caracter "X" y el numero "2"
        Cuando realizo la operación
        Entonces puedo ver el mensaje "Solo se pueden sumar numeros"

    Escenario: No acepta caracteres
        Dado que ingreso el numero "-5" y el numero "2"
        Cuando realizo la operación
        Entonces puedo ver el mensaje "Solo se puede sumar numeros positivos y el cero"

    Escenario: Sumar 2 más 2
        Dado que ingreso el numero "2" y el numero "2"
        Cuando realizo la operación
        Entonces puedo ver el resultado "4"

    Escenario: Sumar 3 más 2
        Dado que ingreso el numero "3" y el numero "2"
        Cuando realizo la operación
        Entonces puedo ver el resultado "5"

    Escenario: Sumar caracter y numero
        Dado que ingreso el caracter "X" y el numero "2"
        Cuando realizo la operación
        Entonces puedo ver el mensaje "Solo se pueden sumar numeros"

    Escenario: Sumar numero negativo y numero
        Dado que ingreso el numero "-2" y el numero "2"
        Cuando realizo la operación
        Entonces puedo ver el mensaje "Solo se puede sumar numeros positivos y el cero"

    Escenario: Sumar numero flotante y numero
        Dado que ingreso el flotante "4.5" y el numero "2"
        Cuando realizo la operación
        Entonces puedo ver el mensaje "Solo se puede sumar numeros enteros"

    Escenario: Sumar cero y un numero
        Dado que ingreso el numero "0" y el numero "5"
        Cuando realizo la operación
        Entonces puedo ver el resultado "5"

    Escenario: Sumar cero y cero
        Dado que ingreso el numero "0" y el numero "0"
        Cuando realizo la operación
        Entonces puedo ver el resultado "0"

    Escenario: Sumar numeros grandes
        Dado que ingreso el numero "1000" y el numero "2000"
        Cuando realizo la operación
        Entonces puedo ver el resultado "3000"