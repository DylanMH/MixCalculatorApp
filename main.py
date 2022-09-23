from email.policy import default
import re
import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang.builder import  Builder

# Only accept number values as text inputs        
class FloatInput(TextInput):
        
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join(
                re.sub(pat, '', s)
                for s in substring.split('.', 1)
            )
        return super().insert_text(s, from_undo=from_undo)

# Main Class
class PageLayout(GridLayout):
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
            self.ids.button_output.text = "Please enter a valid number"
    pass

# Build the mainwidget.kv file
class MainWidgetApp(App):
    def build(self):
        return PageLayout()

# Runs the app
if __name__ == '__main__':
    MainWidgetApp().run()
