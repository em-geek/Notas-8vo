from datetime import datetime

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def convertir_fecha(fecha):
    meses = {
        1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
        7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
    }
    
    numeros = {
        0: "Cero", 1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco", 6: "Seis",
        7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez", 11: "Once", 12: "Doce",
        13: "Trece", 14: "Catorce", 15: "Quince", 16: "Dieciséis", 17: "Diecisiete",
        18: "Dieciocho", 19: "Diecinueve", 20: "Veinte", 21: "Veintiuno", 22: "Veintidós",
        23: "Veintitrés", 24: "Veinticuatro", 25: "Veinticinco", 26: "Veintiséis",
        27: "Veintisiete", 28: "Veintiocho", 29: "Veintinueve", 30: "Treinta",
        31: "Treinta y uno"
    }
    
    if not fecha:
        return 'La entrada no debe de estar vacia'
    
    partes = fecha.split('/')
    
    if len(partes) != 3:
        return 'El formato proporcionado no se detecta como una fecha DD/MM/AAAA'
    
    try:
        dia, mes, anio = map(int, partes)
    except ValueError:
        return 'El dia, mes y año debe estar escrito en numero'
    
    if anio < 1800:
        return 'Fecha invalida, el año no debe ser menor a 1800.'
    
    hoy = datetime.today()
    if anio > hoy.year or (anio == hoy.year and mes > hoy.month) or (anio == hoy.year and mes == hoy.month and dia > hoy.day):
        return 'La fecha debe de estar dentro del rango desde 1800 hasta la fecha actual'
    
    if mes not in meses:
        return 'El mes proporcionado no existe'
    
    dias_mes = {1: 31, 2: 29 if es_bisiesto(anio) else 28, 3: 31, 4: 30, 5: 31, 6: 30, 
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    if dia < 1 or dia > dias_mes[mes]:
        return 'El dia proporcionado no existe'
    
    texto = f"{numeros[dia]} de {meses[mes]} de {convertir_anio(anio)}"
    
    return texto

def convertir_anio(anio):
    if anio == 2000:
        return "dos mil"

    if anio < 2000:
        mil = "mil"
        anio -= 1000
    else:
        mil = "dos mil"
        anio -= 2000

    especiales = {
        10: "diez", 11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
        16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve",
        20: "veinte", 21: "veintiuno", 22: "veintidós", 23: "veintitrés",
        24: "veinticuatro", 25: "veinticinco", 26: "veintiséis",
        27: "veintisiete", 28: "veintiocho", 29: "veintinueve", 30: "treinta",
        40: "cuarenta", 50: "cincuenta", 60: "sesenta", 70: "setenta", 
        80: "ochenta", 90: "noventa"
    }

    centenas = {
        100: "cien", 200: "doscientos", 300: "trescientos", 400: "cuatrocientos",
        500: "quinientos", 600: "seiscientos", 700: "setecientos", 
        800: "ochocientos", 900: "novecientos"
    }

    if anio == 0:
        return mil

    if anio in especiales:
        return f"{mil} {especiales[anio]}"

    c = (anio // 100) * 100
    d = (anio % 100)

    texto = mil

    if c in centenas:
        texto += f" {centenas[c]}"

    if d in especiales:
        texto += f" {especiales[d]}"
    elif d > 0:
        decena = (d // 10) * 10
        unidad = d % 10
        if decena in especiales:
            texto += f" {especiales[decena]}"
        if unidad > 0:
            texto += f" y {especiales[unidad]}"

    return texto.strip()
