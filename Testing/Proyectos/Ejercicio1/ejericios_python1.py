# -*- coding: utf-8 -*-
'''
Trabajo realizado por José Emmanuel Sandoval Sanchez y Joel Salas Moreno
'''


def minutos_de_la_semana(semanas):
    """

    >>> minutos_de_la_semana(1)
    10080

    >>> minutos_de_la_semana(2)
    20160
    """
    return 10080 * semanas


def obtener_residuo_sin_mod(numerador, divisor):
    """
    >>> obtener_residuo_sin_mod(28,7)
    0
    >>> obtener_residuo_sin_mod(30,7)
    2
    """
    num = numerador
    while (num >= divisor):
        num = num - divisor
    return num


def divisible_entre_3(numero):
    """
    >>> divisible_entre_3(9)
    True
    >>> divisible_entre_3(7)
    False
    """
    num = numero/3
    if (num.is_integer()):
        return True
    else:
        return False


def cuadrado_de_un_conjunto(numeros):
    """
    Given a set of numbers return a set of the numbers squared
    >>> cuadrado_de_un_conjunto({1,2,3,4,5,5,5})
    {1, 4, 9, 16, 25}
    """
    return {x ** 2 for x in numeros}


def potencia_de_2_en_conjunto(numeros):
    """
    >>> potencia_de_2_en_conjunto({0,1,2,3,4})
    {0, 1, 4, 9, 16}
    """
    return {x**2 for x in numeros}


def producto_de_dos_conjuntos(xs, ys):
    """
    >>> producto_de_dos_conjuntos({1,2,3},{3,4,5})
    {3, 4, 5, 6, 8, 9, 10, 12, 15}
    """
    resultado = set()
    for x in xs:
        for y in ys:
            resultado.add(x * y)
    return resultado


def producto_de_conjuntos_sin_duplicados(xs, ys):
    """
    >>> producto_de_conjuntos_sin_duplicados({1,2,3},{3,4,5})
    {3, 4, 5, 6, 8, 9, 10, 12, 15}
    """
    resultado = set()
    for x in xs:
        for y in ys:
            resultado.add(x * y)
    return resultado


def interseccion(Ss, Ts):
    """
    >>> interseccion({1, 2, 3, 4},{3, 4, 5, 6})
    {3, 4}
    """
    resultado = set()  # Conjunto vacío para almacenar la intersección
    for elemento in Ss:
        if elemento in Ts:  # Si el elemento está en ambos conjuntos
            resultado.add(elemento)
    return resultado


def promedio_de_lista(lista):
    """
    >>> promedio_de_lista([20, 10, 15, 75])
    30
    """
    contador = 0
    sumador = 0
    for x in lista:
        sumador = sumador + x
        contador = contador + 1
    return int(sumador/contador)


def producto_cartesiano(Xs, Ys):
    """
    >>> producto_cartesiano(['A','B','C'],[1,2,3])
    [['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2], ['B', 3], ['C', 1], ['C', 2], ['C', 3]]
    """
    resultado = []  # Lista vacía para almacenar los pares
    for x in Xs:
        for y in Ys:
            resultado.append([x, y])  # Agregamos la combinación como lista
    return resultado
