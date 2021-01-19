#Librerias
from bs4 import BeautifulSoup
import requests
import pandas as pd


#inicializamos el navegador
urlMontevideo = 'https://www.accuweather.com/es/uy/montevideo/349269/daily-weather-forecast/349269'
agent = {"User-Agent":"Mozilla/5.0"}
page = requests.get(urlMontevideo, headers=agent).text
soup = BeautifulSoup(page, 'html.parser')

#DIAS
listdia = soup.find_all('span', class_ = 'module-header dow date')
dia = list()

count = 0
for i in listdia:
    if count < 7:
        dia.append(i.text)
    else:
        break
    count += 1

#FECHAS
listfecha = soup.find_all('span', class_ = 'module-header sub date')
fecha = list()
count = 0
for i in listfecha:
    if count < 7:
        fecha.append(i.text)
    else:
        break
    count += 1

#TEMPERATURA ALTA
listtempalt = soup.find_all('span', class_ = 'high')
tempalta = list()
count = 0
for i in listtempalt:
    if count < 7:
        tempalta.append(i.text)
    else:
        break
    count += 1

#TEMPERATURA BAJA
listtempbaja = soup.find_all('span', class_ = 'low')
tempabaja = list()
count = 0
for i in listtempbaja:
    if count < 7:
        tempabaja.append(i.text)
    else:
        break
    count += 1

#DESCRIPCION
listdescripcion = soup.find_all('div', class_ = 'phrase')
descripcion = list()
count = 0
for i in listdescripcion:
    if count < 7:
        i = i.text.replace('\n', '')
        i = i.replace('\t', '')
        descripcion.append(i)
    else:
        break
    count += 1

#PROBABILIDAD DE LLUVIA
listlluvia = soup.find_all('div', class_ = 'precip')
lluvia = list()
count = 0
for i in listlluvia:
    if count < 7:
        i = i.text.replace('\n', '')
        i = i.replace('\t', '')
        i = i.replace('\xa0%', '')
        lluvia.append(i)
    else:
        break
    count += 1

df = pd.DataFrame({'Dias': dia, 'Fecha': fecha, 'Grados Max': tempalta, 'Grados min' : tempabaja ,'Estado': descripcion, 'Prov. de lluvia': lluvia})
print(df)
