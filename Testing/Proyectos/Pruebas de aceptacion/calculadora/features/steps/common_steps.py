from behave import given, when, then
from calculadora import Calculadora

@given('que ingreso el número "{num1}" y el número "{num2}"')
def step_ingresar_numeros(context, num1, num2):
    context.calc = Calculadora
    context.num1 = int(num1)
    context.num2 = int(num2)

@given(u'que ingreso el flotante "{num1}" y el número "{num2}"')
def step_impl_flotante(context, num1, num2):
    context.calc = Calculadora
    context.num1 = float(num1)
    context.num2 = int(num2)


@given(u'que ingreso el caracter "{caracter}" y el número "{num2}"')
def step_impl_caracter(context, caracter, num2):
    context.calc = Calculadora
    context.num1 = caracter
    context.num2 = int(num2)

@then(u'puedo ver el mensaje "{mensaje}"')
def step_impl_mensaje(context, mensaje):
    assert context.resultado == mensaje, f'El resultado es {context.resultado} y el esperado es {mensaje}'

@then(u'puedo ver el resultado "{esperado}"')
def step_impl_resultado(context, esperado):
    assert context.resultado == int(esperado), f'El resultado es {context.resultado} y el esperado es {esperado}'
