from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton

API_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ua"

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(name="home_screen", **kwargs)

    def city_request(self):
        city = self.ids.text.lower().strip()
        api_args = {
            "q": city,
            "appid": API_KEY
        }
        data = requests.get(API_URL, api_args)
        response = data.json()
        print(response)

class MyWeatherApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        Builder.load_file('style.kv')
        return HomeScreen()

MyWeatherApp().run()