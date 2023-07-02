from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_hex_from_color

class Container(BoxLayout):    
    def button_click(self, color, color_name):
        self.label.text = color_name
        self.text_input.text = get_hex_from_color(color)

class MyApp(App):
    def build(self):
        Window.size = 360, 800
        return Container()

if __name__ == "__main__":
    MyApp().run()