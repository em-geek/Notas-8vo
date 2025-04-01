from behave import given, when, then
from years import Years

@given('que ingreso la fecha "{entrada}"')
def step_ingreso_fecha(context, entrada):
    context.entrada = entrada

@given('que ingreso la fecha ""')
def step_ingreso_fecha(context):
    context.entrada = None

@when('realizo la conversión de la fecha')
def step_conversion(context):
    years = Years()
    context.resultado = years.convertir_fecha(context.entrada)

@then('puedo ver el mensaje "{resultado}"')
def step_ver_mensaje(context, resultado):
    assert context.resultado == resultado, f"Esperado: {resultado}, obtenido: {context.resultado}"

@then('puedo ver la fecha en palabras "{resultado}"')
def step_ver_fecha(context, resultado):
    assert context.resultado == resultado, f"Esperado: {resultado}, obtenido: {context.resultado}"
