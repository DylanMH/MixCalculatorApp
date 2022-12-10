__version__ = 1.0
import re

import kivy

import kivymd

import os
kivy.require('2.1.0')

#KivyMD Imports
from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextField
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem
#Kivy Imports
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang.builder import  Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import sync_pixel_scale, dispatch_pixel_scale
from kivy.properties import ColorProperty
from kivy.core.window import Window
from kivy.clock import Clock



# Only accept number values as text inputs        
class FloatInput(MDTextField):
    box_color = ColorProperty('orange')
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
class MenuScreen(Screen):
    pass

# Page Layout and Functions of the Mix Page
class MixLayout(Screen):
    def calculations(self):
        try:
            length = float(self.ids.length_input.text)
            width = float(self.ids.width_input.text)
            area = length * width
            depth_in_feet = float(self.ids.depth_input.text) / 12
            cubic_feet = area * depth_in_feet
            density = float(self.ids.density_input.text)
            mix_total = round((cubic_feet * density) / 2000 + 5, 2)
            self.ids.button_output.text = str(mix_total) + " Tons!"
        except:
            self.ids.button_output.text = "Calculate Total"
    pass

# Page Layout and Functions for the Concrete Page
class ConLayout(Screen):
    def calculations(self):
        self.ids.button_output.text = ""
        try:
            length = float(self.ids.length_input.text)
            width = float(self.ids.width_input.text)
            area = length * width
            thickness = float(self.ids.thickness_input.text) / 12
            cubic_feet = thickness * area
            total_yards = round(cubic_feet * .037, 2)
            self.ids.button_output.text = str(total_yards) + " Yards!"
        except:
            self.ids.button_output.text = "Calculate Total"
    pass

# Page Layout and Functions for Baserock Page
class RockLayout(Screen):
    def calculations(self):
        self.ids.button_output.text = ""
        try:
            length = float(self.ids.length_input.text)
            width = float(self.ids.width_input.text)
            area = length * width
            depth = float(self.ids.depth_input.text) / 12
            cubic_feet = depth * area
            total_tons = round(cubic_feet / 21.6, 2)
            self.ids.button_output.text = str(total_tons) + " Tons!"
        except:
            self.ids.button_output.text = "Calculate Total"
    pass

# Page Layout and Function for Rebar
class RebarLayout(Screen):
    def calculations(self):
        self.ids.button_output.text = ""
        try:
            #User inputed variables
            slab_length = float(self.ids.length_input.text)
            slab_width = float(self.ids.width_input.text)
            rebar_grid = float(self.ids.grid_input.text)
            length_rebar = float(self.ids.rebar_length_input.text)
            #Default Variable
            edge_grid = 3/12
            #Calculated Variables
            grid_length_inches = ((slab_length - (2 * edge_grid)) * 12)
            grid_width_inches = ((slab_width - (2 * edge_grid)) * 12)
            rebar_colums = round(grid_length_inches / rebar_grid)
            rebar_rows = round(grid_width_inches / rebar_grid)
            total_rebar_length = (rebar_colums * slab_width) + (rebar_rows * slab_length)
            total_rebar_needed = round(total_rebar_length / length_rebar)

            self.ids.button_output.text = str(total_rebar_needed) + " sticks of rebar"
        except:
            self.ids.button_output.text = "Calculate Total"

class DowelLayout(Screen):
    def calculations(self):
        self.ids.button_output.text = ""
        try:
            #Calculation for dowels
            perimeter = (2 * (float(self.ids.length_input.text) + float(self.ids.width_input.text))) * 12
            total_dowels = round(perimeter / float(self.ids.dowel_input.text))

            self.ids.button_output.text = str(total_dowels) + " dowels"
        except:
            self.ids.button_output.text = "Calculate Total"

# Build the mainapp.kv file
class MainApp(MDApp):
    # Builds the window manager
    sm = ScreenManager()
    
    def build(self):
        self.sm.add_widget(MenuScreen(name="main"))
        self.sm.add_widget(MixLayout(name="mix"))
        self.sm.add_widget(ConLayout(name="concrete"))
        self.sm.add_widget(RockLayout(name="baserock"))
        self.sm.add_widget(RebarLayout(name="rebar"))
        self.sm.add_widget(DowelLayout(name="dowel"))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Amber'
        return MainApp.sm

    ###############################################################################################################
        # Allows the changing of screens with header buttons and also changes the theme styles of specific windows
    ###############################################################################################################
    def change_screen(self, screen):
        self.sm.current = screen
        if self.sm.current == "main":
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'Amber'
        else:
            self.theme_cls.theme_style = 'Dark'
            self.theme_cls.primary_palette = 'Orange'


# Runs the app
if __name__ == '__main__':
    MainApp().run()