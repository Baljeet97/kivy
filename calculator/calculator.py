from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class CalculatorApp(App):

    def build(self):
        return Calculating()


class Calculating(GridLayout):

    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

    def pi(self, value):
        result = value ** 2
        self.display.text = int(result)


CalculatorApp().run()
