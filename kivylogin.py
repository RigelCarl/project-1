from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen


class testApp(Screen):
    def __init___(self, **kwargs):
        super().__init__(**kwargs)

    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"

        return testApp()


if __name__ == "__main__":
    Window.size = (360, 640)  # Don't use any size for android or ios
    Builder.load_file("main.kv")  # If the file in same folder else location
    MyApp().run()
