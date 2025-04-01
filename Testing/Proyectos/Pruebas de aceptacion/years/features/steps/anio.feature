Característica: Convertir fecha a texto
    Como usuario de la aplicación
    Quiero convertir una fecha en formato DD/MM/AAAA a su representación textual
    Para obtener una descripción legible de la fecha

    Escenario: Fecha menor a 1800
        Dado que ingreso la fecha "21/11/1780"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "Fecha invalida, el año no debe ser menor a 1800."

    Escenario: Mes inválido
        Dado que ingreso la fecha "21/13/1980"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "El mes proporcionado no existe"

    Escenario: Día inválido en año no bisiesto
        Dado que ingreso la fecha "29/02/2023"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "El dia proporcionado no existe"

    Escenario: Fecha fuera de rango
        Dado que ingreso la fecha "24/06/2025"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "La fecha debe de estar dentro del rango desde 1800 hasta la fecha actual"

    Escenario: Mes con doble dígito extra
        Dado que ingreso la fecha "29/022/2024"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "El mes proporcionado no existe"

    Escenario: Formato inválido (texto)
        Dado que ingreso la fecha "HOLA"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "El formato proporcionado no se detecta como una fecha DD/MM/AAAA"

    Escenario: Formato inválido (guiones)
        Dado que ingreso la fecha "01-02-2021"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "El formato proporcionado no se detecta como una fecha DD/MM/AAAA"

    Escenario: Ceros en la fecha
        Dado que ingreso la fecha "00/00/0000"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "Fecha invalida, el año no debe ser menor a 1800."

    Escenario: Caracteres no numéricos
        Dado que ingreso la fecha "XX/01/2025"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "El dia, mes y año debe estar escrito en numero"

    Escenario: Cadena vacía
        Dado que ingreso la fecha ""
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "La entrada no debe de estar vacia"

    Escenario: Fecha válida fuera de rango
        Dado que ingreso la fecha "10/03/2026"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "La fecha debe de estar dentro del rango desde 1800 hasta la fecha actual"

    Escenario: Fecha extremadamente antigua
        Dado que ingreso la fecha "01/01/1750"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver el mensaje "Fecha invalida, el año no debe ser menor a 1800."

    Escenario: Fecha correcta en palabras
        Dado que ingreso la fecha "21/11/1980"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver la fecha en palabras "Veintiuno de noviembre de mil novecientos ochenta"

    Escenario: Fecha bisiesto válida
        Dado que ingreso la fecha "29/02/2024"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver la fecha en palabras "Veintinueve de febrero de dos mil veinticuatro"

    Escenario: Fecha válida mil
        Dado que ingreso la fecha "10/03/2000"
        Cuando realizo la conversión de la fecha
        Entonces puedo ver la fecha en palabras "Diez de marzo de dos mil"
