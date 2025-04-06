from behave import when, given, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep


@given(u'le doy click al menú Programas, luego click en el submenú Lista')
def step_impl(context):
    #Dependeiendo la computadora si el programa no funciona se requiere comentar esta linea
    context.driver.find_element(By.CLASS_NAME, 'fas').click()
    sleep(0.5)
    context.driver.find_element(By.PARTIAL_LINK_TEXT, 'Programas').click()
    sleep(0.5)
    context.driver.find_element(By.PARTIAL_LINK_TEXT, 'Lista').click()
    sleep(3)



@when(u'presiono el boton Eliminar del programa "{programa}"')
def step_impl(context, programa):
    filas = context.driver.find_elements(By.CSS_SELECTOR, '#tbodyResultados tr')
    
    for fila in filas:
        columnas = fila.find_elements(By.TAG_NAME, "td")
        if len(columnas) >= 3:
            programaBusqueda = columnas[0].text.strip()

            if programaBusqueda == programa:
                context.driver.find_element(By.LINK_TEXT, "Eliminar").click()
                sleep(2)
                context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Eliminar']").click()
                sleep(2)


@then(u'puedo ver que el programa "{programa}" no esta en la lista de programas.')
def step_impl(context, programa):
    tbody = context.driver.find_element(By.ID, 'tbodyResultados')
    unidades = []
    for tr in tbody.find_elements(By.TAG_NAME, 'tr'):
        td = tr.find_elements(By.TAG_NAME, 'td')
        unidades.append(td[0].text)
    assert programa not in unidades, \
        f"El programa {programa} si se encuentra en la lista de programa"
    context.driver.quit() 
