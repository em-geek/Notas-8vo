from behave import given, when, then
from calculadora import Calculadora

@given(u'que ingreso el numero "{num1}" y el numero "{num2}"')
def step_impl(context, num1, num2):
    context.calc = Calculadora
    context.num1 = int(num1)
    context.num2 = int(num2)

@given(u'que ingreso el flotante "{num1}" y el numero "{num2}"')
def step_impl(context, num1, num2):
    context.calc = Calculadora
    context.num1 = float(num1)
    context.num2 = int(num2)

@given(u'que ingreso el caracter "{caracter}" y el numero "{num2}"')
def step_impl(context, caracter, num2):
    context.calc = Calculadora
    context.num1 = caracter
    context.num2 = int(num2)

@when(u'realizo la operación')
def step_impl(context):
    context.resultado = context.calc.sumar(context.num1, context.num2)


@then(u'puedo ver el resultado "{esperado}"')
def step_impl(context, esperado):
    assert context.resultado == int(esperado), f'El resultado es {context.resultado} y el esperado es {esperado}'

@then(u'puedo ver el mensaje "{mensaje}"')
def step_impl(context, mensaje):
    assert context.resultado == mensaje, f'El resultado es {context.resultado} y el esperado es {mensaje}'
