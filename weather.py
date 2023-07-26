from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
import requests
from config import *
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

API_URL = "https://api.openweathermap.org/data/2.5/weather?&units=metric&lang=ua"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast/daily?cnt=7&units=metric&lang=ua"

class WeatherCard(MDCard):
    super().__init__()
    def __init__(self, temp, weather_text, winf_speed, rain, rain_pop=None):
        self.ids.weather_text.text = weather_text.capitalize()
        self.ids.temp_text.text = str(round(temp)) + "C°"
        if rein_pop:
            self.ids.rein_pop_text.text = f"Ймовірність опадів: {round(rain_pop)}%"
        self.ids.rein_text.text = f"Кількість опадів: {rain} ММ"
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
        data = requests.get(API_URL, api_args)
        response = data.json()
        temp_data = response['main']['temp']
        weather_data = response['weather'][0]['temp']
        desc_data = response['weather'][0]['description']
        wind_data = response['wind']['speed']
        rain_data = response['rain']['1h']
        new_card = Weather_card(temp_data, weather_data, wind_data, rain_data)
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