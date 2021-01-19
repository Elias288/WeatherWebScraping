from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk

class scriping:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Weather Bot')

        ttk.Label(window, text="Elija departamento").grid(row=0, column=0)
        n = tk.StringVar()
        self.combo = ttk.Combobox(window, width= 27, textvariable = n)
        self.combo['values'] = ('Montevideo', 'Paysandú', 'Durazno', 'Artigas')
        self.combo.grid(row=0, column=1)
        self.combo.current(0)

        ttk.Button(window, text='Obtener informe de clima', command= self.obtener).grid(row=0, column=2)

        self.message = Label(text = '', fg = 'red')
        self.message.grid(row=2, column= 1)

        columns = ('#1', '#2', '#3', '#4', '#5', '#6')
        self.tree = ttk.Treeview(window, columns=columns, show='headings')
        self.tree.grid(row= 3, column=0, columnspan=3)
        self.tree.column("#1", minwidth=0, width=100, stretch=NO)
        self.tree.column("#2", minwidth=0, width=50, stretch=NO)
        self.tree.column("#3", minwidth=0, width=100, stretch=NO)
        self.tree.column("#4", minwidth=0, width=100, stretch=NO)
        self.tree.column("#5", minwidth=0, width=150, stretch=NO)
        self.tree.column("#6", minwidth=0, width=100, stretch=NO)

        self.tree.heading('#1', text='Dia')
        self.tree.heading('#2', text='Fecha')
        self.tree.heading('#3', text='Temp. Max')
        self.tree.heading('#4', text='Temp. Min')
        self.tree.heading('#5', text='Descripcion')
        self.tree.heading('#6', text='Prob. lluvia')

    def info(self):
        url = ''
        if self.combo.get() == 'Montevideo':
            self.message['text'] = ''
            url = 'https://www.accuweather.com/es/uy/montevideo/349269/daily-weather-forecast/349269'
        if self.combo.get() == 'Paysandú':
            self.message['text'] = ''
            url = 'https://www.accuweather.com/es/uy/paysandu/350474/daily-weather-forecast/350474'
        if self.combo.get() == 'Durazno':
            self.message['text'] = ''
            url = 'https://www.accuweather.com/es/uy/durazno/347830/daily-weather-forecast/347830'
        if self.combo.get() == 'Artigas':
            self.message['text'] = ''
            url = 'https://www.accuweather.com/es/uy/artigas/347277/daily-weather-forecast/347277'

        if url != '':
            agent = {"User-Agent": "Mozilla/5.0"}
            page = requests.get(url, headers=agent).text
            soup = BeautifulSoup(page, 'html.parser')

            #SEPARAR
            # DIAS
            listdia = soup.find_all('span', class_='module-header dow date')
            self.dia = list()

            count = 0
            for i in listdia:
                if count < 7:
                    self.dia.append(i.text)
                else:
                    break
                count += 1

            # FECHAS
            listfecha = soup.find_all('span', class_='module-header sub date')
            self.fecha = list()
            count = 0
            for i in listfecha:
                if count < 7:
                    self.fecha.append(i.text)
                else:
                    break
                count += 1

            # TEMPERATURA ALTA
            listtempalt = soup.find_all('span', class_='high')
            self.tempalta = list()
            count = 0
            for i in listtempalt:
                if count < 7:
                    self.tempalta.append(i.text)
                else:
                    break
                count += 1

            # TEMPERATURA BAJA
            listtempbaja = soup.find_all('span', class_='low')
            self.tempabaja = list()
            count = 0
            for i in listtempbaja:
                if count < 7:
                    i = i.text.replace('/', '')
                    self.tempabaja.append(i)
                else:
                    break
                count += 1

            # DESCRIPCION
            listdescripcion = soup.find_all('div', class_='phrase')
            self.descripcion = list()
            count = 0
            for i in listdescripcion:
                if count < 7:
                    i = i.text.replace('\n', '')
                    i = i.replace('\t', '')
                    self.descripcion.append(i)
                else:
                    break
                count += 1

            # PROBABILIDAD DE LLUVIA
            listlluvia = soup.find_all('div', class_='precip')
            self.lluvia = list()
            count = 0
            for i in listlluvia:
                if count < 7:
                    i = i.text.replace('\n', '')
                    i = i.replace('\t', '')
                    i = i.replace('\xa0%', '')
                    self.lluvia.append(i)
                else:
                    break
                count += 1

    def obtener(self):
        if self.combo.get() == '':
            self.message['text'] = 'Elija un departamento'
        else:
            self.info()

            # cleaning table
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)

            fila = []
            for n in range(7):
                fila.append((self.dia[n], self.fecha[n], self.tempalta[n], self.tempabaja[n], self.descripcion[n], self.lluvia[n]))

            for x in fila:
                self.tree.insert('', tk.END, values=x)

if __name__ == '__main__':
    window = Tk()
    application = scriping(window)
    window.mainloop()
