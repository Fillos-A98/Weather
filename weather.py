from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
import requests
from config import *
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
import datetime

API_URL = "https://api.openweathermap.org/data/2.5/weather?&units=metric&lang=ua"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast?&cnt=7&units=metric&lang=ua"

class WeatherCard(MDCard):
    def __init__(self, date, temp, weather_text, winf_speed, rain, rain_pop=None):
        super().__init__()
        self.ids.date_text.text = date
        self.ids.weather_text.text = weather_text.capitalize()
        self.ids.temp_text.text = str(round(temp)) + "C°"
        if rain_pop:
            self.ids.rein_pop_text.text = f"Ймовірність опадів: {round(rain_pop)}%"
        self.ids.rain_text.text = f"Кількість опадів: {rain} ММ"
        self.ids.wind_speed_text.text = f"Швидкісь вітру: {rain} М/C"


class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(name="home_screen", **kwargs)

    def city_request(self):
        city = self.ids.city.text.lower().strip()
        api_args = {
            "q": city,
            "appid": API_KEY
        }
        data = requests.get(FORECAST_URL, api_args)
        response = data.json()
        for period in period['list']:
            date_data = period['dt']
            date_obj = datetime.datetime.fromtimestamp(date_data)
            date = date_obj.strftime('%d %b, %H:%M:%S')
            temp_data = period['main']['temp']
            weather_data = period['weather'][0]['main']
            desc_data = period['weather'][0]['description']
            wind_data = period['wind']['speed']
            if 'rain' in period:
                rain_data = period['rain']['3h']
            else:
                rain_data = 0
            rain_pop = period['pop']
            new_card = WeatherCard('now', date_data, temp_data, weather_data, wind_data, rain_data)
            self.ids.weather_carousel.add_widget(new_card)
        print(temp_data)
        print(response)

class MyWeatherApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        Builder.load_file('style.kv')
        self.screen = HomeScreen()
        return self.screen

MyWeatherApp().run()