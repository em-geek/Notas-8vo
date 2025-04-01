Característica: Calcular edad
    Como usuario de el programa
    Deseo saber que soy segun mi edad
    Para tener una descripcion segun mi edad

    Escenario: Edad negativa
        Dado que ingreso mi edad "-1"
        Cuando realizo la operación
        Entonces puedo ver el resultado "No existes"

    Escenario: Niño
        Dado que ingreso mi edad "3"
        Cuando realizo la operación
        Entonces puedo ver el resultado "Eres niño"

    Escenario: Adolescente
        Dado que ingreso mi edad "13"
        Cuando realizo la operación
        Entonces puedo ver el resultado "Eres adolescente"

    Escenario: Adulto
        Dado que ingreso mi edad "20"
        Cuando realizo la operación
        Entonces puedo ver el resultado "Eres adulto"

    Escenario: Adulto Mayor
        Dado que ingreso mi edad "80"
        Cuando realizo la operación
        Entonces puedo ver el resultado "Eres adulto mayor"

    Escenario: Adulto Mayor Limite Superior
        Dado que ingreso mi edad "100"
        Cuando realizo la operación
        Entonces puedo ver el resultado "Eres adulto mayor"

    Escenario: Edad Mumm Raead
        Dado que ingreso mi edad "200"
        Cuando realizo la operación
        Entonces puedo ver el resultado "Eres Mumm-Raead"

    Escenario: Caracter
        Dado que ingreso un caracter "X"
        Cuando realizo la operación
        Entonces puedo ver el resultado "Eres Chabelo"

    Escenario: Edad flotante
        Dado que ingreso mi edad en flotante "19.2"
        Cuando realizo la operación
        Entonces puedo ver el resultado "Los meses no cuentan"

    Escenario: Cero
        Dado que ingreso mi edad "0"
        Cuando realizo la operación
        Entonces puedo ver el resultado "No existes"