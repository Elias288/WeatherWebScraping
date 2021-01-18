from bs4 import BeautifulSoup
import requests
import pandas as pd
#from typing import Optional
#from msedge.selenium_tools import Edge, EdgeOptions
from tkinter import *
from tkinter import ttk

class scriping:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Weather Bot')

        ttk.Button(window, text='Obtener informe de clima', command=self.obtener). grid(row=0, column=1, columnspan=3)

        Label(window, text='Dias',).grid(row=1, column=0)
        Label(window, text='Fecha', ).grid(row=1, column=1)
        Label(window, text='Grados', ).grid(row=1, column=2)
        Label(window, text='Estado', ).grid(row=1, column=3)
        Label(window, text='Prov. de lluvia', ).grid(row=1, column=4)

    def info(self):
        urlMontevideo = 'https://www.accuweather.com/es/uy/montevideo/349269/daily-weather-forecast/349269/'
        page = requests.get(urlMontevideo)
        soup = BeautifulSoup(page.content, 'html.parser')

        eq = soup.find_all('div', class_='daily-wrapper')

        print(eq)

        #SEPARAR
        #datos_semana = info_clima.split(titulo)[1].split('\n')[1:36]


        #return datos_semana

    def obtener(self):
        datos_semana = self.info()
        #datos_semana = ['DOM.', '10/1', '37° /22°', 'Más cálido', '1 %', 'LUN.', '11/1', '28° /18°', 'Algunas severas tormentas', '66 %', 'MAR.', '12/1', '28° /14°', 'Aclarando', '0 %', 'MIÉ.', '13/1', '30° /16°', 'Soleado y agradable', '0 %', 'JUE.', '14/1', '31° /19°', 'Parcialmente soleado', '1 %', 'VIE.', '15/1', '28° /22°', 'Algunas tormentas severas', '67 %', 'SÁB.', '16/1', '32° /14°', 'Potentes tormentas temprano', '71 %']
        dia = list()
        fecha = list()
        grados = list()
        estado = list()
        humedad = list()

        for i in range(0, len(datos_semana), 5):
            dia.append(datos_semana[i])
            fecha.append((datos_semana[i + 1]))
            grados.append((datos_semana[i + 2]))
            estado.append((datos_semana[i + 3]))
            humedad.append((datos_semana[i + 4]))

        i = 2
        p = 0
        for x in range(7):
            Label(window, text=dia[x]).grid(row= i, column=p)
            Label(window, text=fecha[x]).grid(row=i, column=p + 1)
            Label(window, text=grados[x]).grid(row=i, column=p + 2)
            Label(window, text=estado[x]).grid(row=i, column=p + 3)
            Label(window, text=humedad[x]).grid(row=i, column=p + 4)
            i += 1
            p = 0

if __name__ == '__main__':
    window = Tk()
    application = scriping(window)
    window.mainloop()
