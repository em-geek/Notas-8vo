Característica: Sumar dos números
    Como usuario de la calculadora 
    Deseo sumar dos números
    Para tener cálculos precisos

    Escenario: Sumar 2 mas 2
        Dado que ingreso el número "2" y el número "2"
        Cuando realizo la operación
        Entonces puedo ver el resultado "4"

    Escenario: Sumar 5 mas 2
        Dado que ingreso el número "5" y el número "2"
        Cuando realizo la operación
        Entonces puedo ver el resultado "7"

    Escenario: No acepta caracteres
        Dado que ingreso el caracter "X" y el número "2"
        Cuando realizo la operación
        Entonces puedo ver el mensaje "Solo se pueden sumar numeros"

    Escenario: No acepta caracteres
        Dado que ingreso el número "-5" y el número "2"
        Cuando realizo la operación
        Entonces puedo ver el mensaje "Solo se puede sumar numeros positivos y el cero"

    Escenario: Sumar 2 más 2
        Dado que ingreso el número "2" y el número "2"
        Cuando realizo la operación
        Entonces puedo ver el resultado "4"

    Escenario: Sumar 3 más 2
        Dado que ingreso el número "3" y el número "2"
        Cuando realizo la operación
        Entonces puedo ver el resultado "5"

    Escenario: Sumar caracter y número
        Dado que ingreso el caracter "X" y el número "2"
        Cuando realizo la operación
        Entonces puedo ver el mensaje "Solo se pueden sumar numeros"

    Escenario: Sumar número negativo y número
        Dado que ingreso el número "-2" y el número "2"
        Cuando realizo la operación
        Entonces puedo ver el mensaje "Solo se puede sumar numeros positivos y el cero"

    Escenario: Sumar número flotante y número
        Dado que ingreso el flotante "4.5" y el número "2"
        Cuando realizo la operación
        Entonces puedo ver el mensaje "Solo se puede sumar numeros enteros"

    Escenario: Sumar cero y un número
        Dado que ingreso el número "0" y el número "5"
        Cuando realizo la operación
        Entonces puedo ver el resultado "5"

    Escenario: Sumar cero y cero
        Dado que ingreso el número "0" y el número "0"
        Cuando realizo la operación
        Entonces puedo ver el resultado "0"

    Escenario: Sumar números grandes
        Dado que ingreso el número "1000" y el número "2000"
        Cuando realizo la operación
        Entonces puedo ver el resultado "3000"