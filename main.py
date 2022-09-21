from email.policy import default
import re
import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

        
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


class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2
        # Length Widget
        self.add_widget(Label(text = "Length"))
        self.length_side = FloatInput(multiline = False, hint_text = str(0))
        self.add_widget(self.length_side)
        # Width Widget
        self.add_widget(Label(text = "Width"))
        self.width_side = FloatInput(multiline = False, hint_text = str(0))
        self.add_widget(self.width_side)
        # Depth in Inches
        self.add_widget(Label(text = 'Depth In Inches'))
        self.depth = FloatInput(multiline = False, hint_text = str(0))
        self.add_widget(self.depth)
        # Button Widget
        self.button = Button(text = "CALCULATION")
        self.button.bind(on_press = self.calculations)
        self.add_widget(self.button)
        # Area Widget
        self.mix_total = Label(text = "")
        self.add_widget(self.mix_total)

    def calculations(self, instance):
        length = float(self.length_side.text)
        width = float(self.width_side.text)
        area = length * width
        depth_in_feet = float(self.depth.text) / 12
        cubic_feet = area * depth_in_feet
        mix_total = (cubic_feet * 145) / 2000
        self.mix_total.text = 'Total Hot Mix Needed = ' + str(mix_total)





       
class MyApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()
