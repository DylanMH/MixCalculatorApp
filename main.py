import re
import kivy

from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextField
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang.builder import  Builder
from kivy.uix.floatlayout import FloatLayout

from kivy.config import Config
Config.set('graphics', 'resizable', True)

# Only accept number values as text inputs        
class FloatInput(MDTextField):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join(re.sub(pat, '', s)
                for s in substring.split('.', 1))
        return super().insert_text(s, from_undo=from_undo)

class WindowManager(ScreenManager):
    pass

# Main Screen
class MainScreen(Screen):
    pass

# Page Layout and Functions of the Mix Page
class MixLayout(Screen):
    def calculations(self):
        self.ids.button_output.text = "Total: "
        try:
            length = float(self.ids.length_input.text)
            width = float(self.ids.width_input.text)
            area = length * width
            depth_in_feet = float(self.ids.depth_input.text) / 12
            cubic_feet = area * depth_in_feet
            mix_total = round((cubic_feet * 145) / 2000, 2)
            self.ids.button_output.text = self.ids.button_output.text + str(mix_total) + " tons!"
        except:
            self.ids.button_output.text = "Please enter a valid number!"
    pass

# Page Layout and Functions for the Concrete Page
class ConLayout(Screen):
    def calculations(self):
        self.ids.button_output.text = "Total: "
        try:
            length = float(self.ids.length_input.text)
            width = float(self.ids.width_input.text)
            area = length * width
            thickness = float(self.ids.thickness_input.text) / 12
            cubic_feet = thickness * area
            total_yards = round(cubic_feet * .037, 2)
            self.ids.button_output.text = self.ids.button_output.text + str(total_yards) + " yards!"
        except:
            self.ids.button_output.text = "Please enter a valid number!"
    pass

# Build the mainapp.kv file
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name="main"))
        self.sm.add_widget(MixLayout(name="mix"))
        self.sm.add_widget(ConLayout(name="concrete"))
        return self.sm

    def change_screen(self, screen):
        self.sm.current = screen


# Runs the app
if __name__ == '__main__':
    MainApp().run()