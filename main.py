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
        self.length_side = FloatInput(multiline = False)
        self.add_widget(self.length_side)
        # Width Widget
        self.add_widget(Label(text = "Width"))
        self.width_side = FloatInput(multiline = False)
        self.add_widget(self.width_side)
        # Button Widget
        self.button = Button(text = "CALCULATION")
        #self.button.bind(on_press = self.calculation)
        self.add_widget(self.button)
        # Area Widget
        self.area_total = Label(text = "Area")
        self.add_widget(self.area_total)
        
class MyApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()
