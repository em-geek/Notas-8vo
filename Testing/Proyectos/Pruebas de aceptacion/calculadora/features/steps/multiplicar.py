from behave import given, when, then
from calculadora import Calculadora
from features.steps.common_steps import step_ingresar_numeros
from features.steps.common_steps import step_impl_flotante

@given(u'que ingreso el caracter "{caracter}" y el numero "{num2}"')
def step_impl_caracter(context, caracter, num2):
    context.calc = Calculadora
    context.num1 = caracter
    context.num2 = int(num2)

@when(u'realizo la operación de multiplicación')
def step_impl_multiplicacion(context):
    context.resultado = context.calc.multiplicar(context.num1, context.num2)

@then(u'puedo ver el resultado "{esperado}"')
def step_impl_resultado_multiplicacion(context, esperado):
    assert context.resultado == int(esperado), f'El resultado es {context.resultado} y el esperado es {esperado}'

@then(u'puedo ver el mensaje "{mensaje}"')
def step_impl_mensaje_multiplicacion(context, mensaje):
    assert context.resultado == mensaje, f'El resultado es {context.resultado} y el esperado es {mensaje}'

