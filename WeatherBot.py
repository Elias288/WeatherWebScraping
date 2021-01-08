#Librerias
from typing import Optional
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge, EdgeOptions

import time
import pandas as pd

#from selenium.webdriver.chrome.options import Options


options = EdgeOptions()
options.use_chromium = True
#options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver_path = 'C:\\Users\\Elias\\Documents\\msedgedriver.exe'

#Opciones de navegacion
driver = Edge(executable_path=driver_path, options=options)

#inicializamos el navegador
driver.get('https://www.accuweather.com/')
Departamento = "Montevideo"

#COOKIES
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div/div[9]/div/div')))\
    .click()

#BUSCADOR
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div/div[1]/div[2]/div[1]/form/input')))\
    .send_keys(Departamento)

#CIUDAD
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div/div[1]/div[2]/div[2]/div[2]/div')))\
    .click()

#DIAS
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div/div[3]/div/div[3]/a[3]')))\
    .click()

card = WebDriverWait(driver, 20)\
    .until(EC.frame_to_be_available_and_switch_to_it((By.NAME,
                                                      "google_ads_iframe_/6581/web/sam/interstitial/weather/local_home_0")))

if(card):
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           "/html/body/div/div/div[1]/div[1]"))).click()

#INFO
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div/div/div[1]/div[1]/div')))

info_clima = driver.find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]')
info_clima = info_clima.text

titulo = driver.find_element_by_css_selector('p.module-title')
titulo = titulo.text
#print(titulo)

#SEPARAR
datos_semana = info_clima.split(titulo)[1].split('\n')[1:36]

dia = list()
fecha = list()
grados = list()
estado = list()
humedad = list()

for i in range(0, len(datos_semana), 5):
    dia.append(datos_semana[i])
    fecha.append((datos_semana[i+1]))
    grados.append((datos_semana[i + 2]))
    estado.append((datos_semana[i + 3]))
    humedad.append((datos_semana[i + 4]))

df = pd.DataFrame({'Dias': dia, 'Fecha': fecha, 'Grados': grados, 'Estado': estado, 'Prov. de lluvia': humedad})
print(df)

df.to_csv('tiempos_de_la_semana.csv', index=False)

driver.quit()
