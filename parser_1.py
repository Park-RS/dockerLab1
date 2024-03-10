import requests
from bs4 import BeautifulSoup



def get_weather(city):
    api_key = 'bd60f287e2f191f1f39ca340d4cf657f'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description']
        }
        
        return weather
    else:
        return None

def main():
    city = 'Барнаул'
    
    weather = get_weather(city)
    if weather:
        print(f'Погода в городе {weather["city"]}:')
        print(f'Температура: {weather["temperature"]}°C')
        print(f'Влажность: {weather["humidity"]}%')
        print(f'Скорость ветра: {weather["wind_speed"]} м/c')
        print(f'Описание: {weather["description"]}')
    else:
        print('Не удалось получить данные о погоде')

if __name__ == '__main__':
    main()