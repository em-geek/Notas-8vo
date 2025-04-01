from behave import given

@given('que ingreso el numero "{num1}" y el numero "{num2}"')
def step_ingresar_numeros(context, num1, num2):
    context.num1 = float(num1)
    context.num2 = float(num2)

@given(u'que ingreso el flotante "{num1}" y el numero "{num2}"')
def step_impl_flotante(context, num1, num2):
    context.calc = Calculadora
    context.num1 = float(num1)
    context.num2 = int(num2)