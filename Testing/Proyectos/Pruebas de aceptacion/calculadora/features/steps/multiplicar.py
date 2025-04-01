from behave import given, when, then
from calculadora import Calculadora
from features.steps.common_steps import step_ingresar_numeros
from features.steps.common_steps import step_impl_flotante
from features.steps.common_steps import step_impl_caracter
from features.steps.common_steps import step_impl_mensaje
from features.steps.common_steps import step_impl_resultado

@when(u'realizo la operación de multiplicación')
def step_impl_multiplicacion(context):
    context.resultado = context.calc.multiplicar(context.num1, context.num2)


