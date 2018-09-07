from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MenuApp(App):

    def build(self):
        Window.size = (500, 500)
        self.title = "Menu"
        self.root = Builder.load_file('menu.kv')
        return self.root


MenuApp().run()
