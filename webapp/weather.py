import requests
import os
from dotenv import load_dotenv

load_dotenv()

def weather_in_city(city_name):
    # URL для запроса погоды
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    # Параметры запроса
    params = {
        "key":os.getenv("API_WEATHER"),
        "q": city_name,
        "format": "json",
        "num_of_days": "5",
        "lang": "ru"
    }
    # Отправка запроса на получение погоды
    try:     
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if "data" in weather:
            if 'weather' in weather["data"]:
                try:
                    return weather['data']['weather']
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False

def weather_in_city_now(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key":os.getenv("API_WEATHER"),
        "q": city_name,
        "format": "json",
        "lang": "ru"
    }
    # Отправка запроса на получение текущей погоды
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if "data" in weather:
        if 'current_condition' in weather["data"]:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False



    


