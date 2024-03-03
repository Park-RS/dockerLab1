import requests
from bs4 import BeautifulSoup

response = requests.get('https://yandex.ru/pogoda/barnaul?lat=53.346785&lon=83.77686')

soup = BeautifulSoup(response.content, 'html.parser')

temp = soup.find('span', class_='temp__value temp__value_with-unit')


print('Текущая погода в Барнауле:', temp.text.strip())