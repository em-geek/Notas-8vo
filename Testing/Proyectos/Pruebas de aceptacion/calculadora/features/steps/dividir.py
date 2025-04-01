from behave import given, when, then
from calculadora import Calculadora
from features.steps.common_steps import step_ingresar_numeros
from features.steps.common_steps import step_impl_flotante

@given(u'que ingreso el caracter "{caracter}" y el numero "{num2}"')
def step_impl_caracter(context, caracter, num2):
    context.calc = Calculadora
    context.num1 = caracter
    context.num2 = int(num2)

@when(u'realizo la operación de división')
def step_impl_division(context):
    context.resultado = context.calc.dividir(context.num1, context.num2)

@then(u'puedo ver el resultado "{esperado}"')
def step_impl_resultado_division(context, esperado):
    # Para dividir el resultado puede ser float, por lo que convertimos según sea necesario
    # En este ejemplo asumimos que el valor esperado se da como string que representa un número
    try:
        valor_esperado = float(esperado)
        assert context.resultado == valor_esperado, f'El resultado es {context.resultado} y el esperado es {esperado}'
    except ValueError:
        # Si no es numérico, se compara directamente el mensaje
        assert context.resultado == esperado, f'El resultado es {context.resultado} y el esperado es {esperado}'

@then(u'puedo ver el mensaje "{mensaje}"')
def step_impl_mensaje_division(context, mensaje):
    assert context.resultado == mensaje, f'El resultado es {context.resultado} y el esperado es {mensaje}'
