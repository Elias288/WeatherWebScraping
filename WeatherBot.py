#Librerias
from bs4 import BeautifulSoup
import requests
import pandas as pd


#inicializamos el navegador
urlMontevideo = 'https://www.accuweather.com/es/uy/montevideo/349269/daily-weather-forecast/349269'
#urlMontevideo = 'https://www.accuweather.com/'
agent = {"User-Agent":"Mozilla/5.0"}
page = requests.get(urlMontevideo, headers=agent).text
soup = BeautifulSoup(page, 'html.parser')

#DIAS
listdia = soup.find_all('span', class_ = 'module-header dow date')
dias = list()

count = 0
for i in listdia:
    if count < 7:
        dias.append(i.text)
    else:
        break
    count += 1

#FECHAS
listfecha = soup.find_all('span', class_ = 'module-header sub date')
fechas = list()
count = 0
for i in listfecha:
    if count < 7:
        fechas.append(i.text)
    else:
        break
    count += 1

#TEMPERATURA ALTA
listtempalt = soup.find_all('span', class_ = 'high')
tempaltas = list()
count = 0
for i in listtempalt:
    if count < 7:
        tempaltas.append(i.text)
    else:
        break
    count += 1

#TEMPERATURA BAJA
listtempbaja = soup.find_all('span', class_ = 'low')
tempabajas = list()
count = 0
for i in listtempbaja:
    if count < 7:
        tempabajas.append(i.text)
    else:
        break
    count += 1

#DESCRIPCION
listdescripciones = soup.find_all('div', class_ = 'phrase')
descripciones = list()
count = 0
for i in listdescripciones:
    if count < 7:
        descripciones.append(i.text)
    else:
        break
    count += 1

#PROBABILIDAD DE LLUVIA
listlluvia = soup.find_all('div', class_ = 'precip')
lluvias = list()
count = 0
for i in listlluvia:
    if count < 7:
        lluvias.append(i.text)
    else:
        break
    count += 1

#print(dias)
#print(fechas)
#print(tempaltas)
#print(tempabajas)
print(descripciones)
print(lluvias)

