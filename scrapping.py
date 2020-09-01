import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://forecast.weather.gov/MapClick.php?lat=28.538230000000055&lon=-81.37738999999993#.Xzgz8OhKjIU'
response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'html.parser')
week = soup.find('div', id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
lista_period = []
lista_short = []
lista_temp = []
for n in range(1, 9):
    x = items[n].find(class_='period-name').get_text()
    lista_period.append(x)
    y = items[n].find(class_='short-desc').get_text()
    lista_short.append(y)
    w = items[n].find(class_='temp').get_text()
    lista_temp.append(w)

wheather_statitics = pd.DataFrame(
    {
        'periodo': lista_period,
        'Descrição': lista_short,
        'Temperatura': lista_temp
    })
print(wheather_statitics)