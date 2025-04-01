from behave import given, when, then
from calculadora import Calculadora
from features.steps.common_steps import step_ingresar_numeros
from features.steps.common_steps import step_impl_flotante
from features.steps.common_steps import step_impl_caracter
from features.steps.common_steps import step_impl_mensaje
from features.steps.common_steps import step_impl_resultado

@when(u'realizo la operación de división')
def step_impl_division(context):
    context.resultado = context.calc.dividir(context.num1, context.num2)

@then(u'puedo ver el resultado "{esperado}" en division')
def step_impl_resultado_division(context, esperado):
    # Para dividir el resultado puede ser float, por lo que convertimos según sea necesario
    # En este ejemplo asumimos que el valor esperado se da como string que representa un número
    try:
        valor_esperado = float(esperado)
        assert context.resultado == valor_esperado, f'El resultado es {context.resultado} y el esperado es {esperado}'
    except ValueError:
        # Si no es numérico, se compara directamente el mensaje
        assert context.resultado == esperado, f'El resultado es {context.resultado} y el esperado es {esperado}'


