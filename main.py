from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import random

Window.clearcolor = (0.06, 0.06, 0.07, 1)

PHONES_DB = [
    {"model": "Samsung A13", "class": "budget", "price": 3500},
    {"model": "Samsung S23", "class": "flagship", "price": 30000},
    {"model": "Motorola G75", "class": "mid", "price": 8000},
    {"model": "Sony Xperia 1 IV", "class": "flagship", "price": 25000},
    {"model": "iPhone 13 Pro", "class": "flagship", "price": 35000},
    {"model": "POCO X6 Pro", "class": "mid", "price": 12000},
    {"model": "Google Pixel 8", "class": "flagship", "price": 32000}
]

STATES = [
    {"name": "убитый", "mult": 0.3, "repair": 1000},
    {"name": "треснул", "mult": 0.5, "repair": 800},
    {"name": "норм", "mult": 0.8, "repair": 300},
    {"name": "идеал", "mult": 1.2, "repair": 0}
]

class GameState:
    def __init__(self):
        self.money = 10000
        self.inventory = []

game = GameState()

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(name="main", **kwargs)
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        self.money_label = Label(text=f"Баланс: {game.money} ₽", size_hint_y=None, height=50, font_size='20sp', bold=True)
        layout.add_widget(self.money_label)

        scroll = ScrollView()
        grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter("height"))

        for phone in PHONES_DB:
            card = BoxLayout(orientation="vertical", size_hint_y=None, height=150, padding=5)
            card.add_widget(Label(text=phone["model"], font_size='14sp', bold=True, color=(1,1,1,1)))
            card.add_widget(Label(text=phone["class"].upper(), font_size='10sp', color=(0.3,0.9,0.9,1)))
            card.add_widget(Label(text=f"{phone['price']} ₽", font_size='14sp', color=(1,0.8,0.3,1)))
            
            btn = Button(text="Купить", size_hint_y=None, height=40, background_color=(0.2,0.4,0.8,1))
            btn.bind(on_release=lambda x, p=phone: self.buy(p))
            card.add_widget(btn)
            grid.add_widget(card)
            
        scroll.add_widget(grid)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def buy(self, phone):
        if game.money >= phone["price"]:
            game.money -= phone["price"]
            self.money_label.text = f"Баланс: {game.money} ₽"

class TechApp(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    TechApp().run()
