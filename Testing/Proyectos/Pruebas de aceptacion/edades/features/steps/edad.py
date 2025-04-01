from behave import given, when, then
from edades import Edades

@given('que ingreso mi edad "{num1}"')
def step_ingresar_numeros(context, num1):
    context.num1 = int(num1)

@given('que ingreso un caracter "{num1}"')
def step_ingresar_numeros(context, num1):
    context.num1 = (num1)

@given('que ingreso mi edad en flotante "{num1}"')
def step_ingresar_numeros(context, num1):
    context.num1 = float(num1)

@when(u'realizo la operación')
def step_impl(context):
    context.edades = Edades
    context.resultado = context.edades.edad(context.num1)

@then(u'puedo ver el resultado "{esperado}"')
def step_impl_resultado(context, esperado):
    assert context.resultado == (esperado), f'El resultado es {context.resultado} y el esperado es {esperado}'