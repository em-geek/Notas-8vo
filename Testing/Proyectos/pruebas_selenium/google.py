from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.bing.com')

busqueda = driver.find_element(By.NAME, 'q')
busqueda.send_keys('ingenieria de software')
time.sleep(5)
busqueda.send_keys(Keys.RETURN)
time.sleep(5)

contenido = driver.find_elements(By.ID, 'b_content')
titulos = driver.find_elements(By.TAG_NAME, 'h2')

print(titulos)
for titulo in titulos:
    print(titulo.text)

#driver.find_element(By.ID, 'search_icon').click()

time.sleep(2)

busqueda = driver.find_element(By.CSS_SELECTOR, 'a.sb_pagN')
time.sleep(2)
busqueda.send_keys(Keys.RETURN)
time.sleep(5)

contenido = driver.find_elements(By.ID, 'b_content')
titulos = driver.find_elements(By.TAG_NAME, 'h2')

print(titulos)
for titulo in titulos:
    print(titulo.text)


time.sleep(20)
