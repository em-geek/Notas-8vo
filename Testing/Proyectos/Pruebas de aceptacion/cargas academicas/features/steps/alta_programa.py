from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

@given(u'le doy click al menú Programas, luego click en el submenú Nuevo')
def step_impl(context):
    #Dependeiendo la computadora si el programa no funciona se requiere comentar esta linea
    context.driver.find_element(By.CLASS_NAME, 'fas').click()
    sleep(0.5)
    context.driver.find_element(By.PARTIAL_LINK_TEXT, 'Programas').click()
    sleep(0.5)
    context.driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo').click()
    sleep(0.5)


@given(u'registró el programa "{nombre}" y su abreviación "{abreviacion}" en la unidad academica de "{unidad}"')
def step_impl(context, nombre, abreviacion, unidad):
    context.driver.find_element(By.NAME, 'nombre').send_keys(nombre)
    context.driver.find_element(By.NAME, 'abreviacion').send_keys(abreviacion)
    select_element = context.driver.find_element(By.NAME, 'unidad_academica')  
    select = Select(select_element)
    
    sleep(1)

    select.select_by_visible_text(unidad)
    sleep(1)


@when(u'presiono el boton Agregar en programas')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-outline-success').click()
    sleep(1)


@then(u'puedo ver el programa "{programa}" en la lista de unidades.')
def step_impl(context, programa):
    tbody = context.driver.find_element(By.ID, 'tbodyResultados')
    unidades = []
    for tr in tbody.find_elements(By.TAG_NAME, 'tr'):
        td = tr.find_elements(By.TAG_NAME, 'td')
        unidades.append(td[0].text)
    assert programa in unidades, \
        f"El programa {programa} no se encuentra en la lista de programa {str(unidades)}"
    context.driver.quit() 