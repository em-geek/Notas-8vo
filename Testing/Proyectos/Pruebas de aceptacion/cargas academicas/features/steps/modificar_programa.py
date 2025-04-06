from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


@given(u'presiono el boton Editar del programa "{programa}"')
def step_impl(context, programa):
    filas = context.driver.find_elements(By.CSS_SELECTOR, '#tbodyResultados tr')
    
    for fila in filas:
        columnas = fila.find_elements(By.TAG_NAME, "td")
        if len(columnas) >= 3:
            programaBusqueda = columnas[0].text.strip()

            if programaBusqueda == programa:
                context.driver.find_element(By.XPATH, "//tr[td[text()='Ingenieria Perrona']]//a[text()='Editar']").click()
                sleep(2)



@given(u'cambio los datos del programa con nombre "{nombre}" y su abreviación "{abreviacion}" en la unidad academica de "{unidad}"')
def step_impl(context, nombre, abreviacion, unidad):
    # Campo 'nombre'
    nombre_input = context.driver.find_element(By.NAME, 'nombre')
    nombre_input.clear()  # Limpia el texto actual
    nombre_input.send_keys(nombre)

    # Campo 'abreviacion'
    abreviacion_input = context.driver.find_element(By.NAME, 'abreviacion')
    abreviacion_input.clear()
    abreviacion_input.send_keys(abreviacion)

    select_element = context.driver.find_element(By.NAME, 'unidad_academica')  
    select = Select(select_element)
    
    sleep(1)

    select.select_by_visible_text(unidad)
    sleep(1)

@given(u'presiono el boton Agregar en programas')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-outline-success').click()
    sleep(1)


@when(u'refresco la vista')
def step_impl(context):
    context.driver.refresh()
