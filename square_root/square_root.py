from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import math


class RootingNumber(App):
    def build(self):
        Window.size = (300, 200)
        self.title = "Square Rooting Number"
        self.root = Builder.load_file('square_root.kv')
        return self.root

    def squaring(self, value):
        result = math.sqrt(value)
        self.root.ids.output_label.text = str(result)


RootingNumber().run()
