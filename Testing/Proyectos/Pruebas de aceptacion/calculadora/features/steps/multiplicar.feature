Característica: Restar dos números
    Como usuario de la calculadora
    Quiero restar dos números
    Para obtener la diferencia correcta

    Escenario: Restar 5 menos 3
        Dado que ingreso el número "5" y el número "3"
        Cuando realizo la operación de resta
        Entonces puedo ver el resultado "2"

    Escenario: Restar 10 menos 0
        Dado que ingreso el número "10" y el número "0"
        Cuando realizo la operación de resta
        Entonces puedo ver el resultado "10"

    Escenario: Restar 0 menos 0
        Dado que ingreso el número "0" y el número "0"
        Cuando realizo la operación de resta
        Entonces puedo ver el resultado "0"

    Escenario: Restar número positivo y negativo
        Dado que ingreso el número "2" y el número "-2"
        Cuando realizo la operación de resta
        Entonces puedo ver el mensaje "Solo se puede restar numeros positivos y el cero"

    Escenario: Restar caracter y número
        Dado que ingreso el caracter "X" y el número "2"
        Cuando realizo la operación de resta
        Entonces puedo ver el mensaje "Solo se pueden restar numeros"

    Escenario: Restar flotante y número
        Dado que ingreso el número "4.5" y el número "2"
        Cuando realizo la operación de resta
        Entonces puedo ver el mensaje "Solo se puede restar numeros enteros"

    Escenario: Restar menor menos mayor
        Dado que ingreso el número "3" y el número "5"
        Cuando realizo la operación de resta
        Entonces puedo ver el resultado "-2"

    Escenario: Restar números iguales
        Dado que ingreso el número "1" y el número "1"
        Cuando realizo la operación de resta
        Entonces puedo ver el resultado "0"

    Escenario: Restar números grandes
        Dado que ingreso el número "9999" y el número "8888"
        Cuando realizo la operación de resta
        Entonces puedo ver el resultado "1111"