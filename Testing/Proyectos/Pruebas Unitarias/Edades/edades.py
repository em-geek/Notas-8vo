def edades(edad):
    if (type(edad) == str):
        return 'Eres Chabelo'
    elif (edad <= 0):
        return 'No existes'
    elif (type(edad) == float):
        return 'Los meses no cuentan'
    elif (edad < 13):
        return 'Eres niño'
    elif (edad < 18):
        return 'Eres adolescente'
    elif (edad < 65):
        return 'Eres adulto'
    elif (edad < 120):
        return 'Eres adulto mayor'
    else: 
        return 'Eres Mumm-Raead'