from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from database.db import create_db
from ui.screens import IntroScreen, LoginScreen, SignUpScreen, UserListScreen

class MainApp(MDApp):
    def build(self):
        create_db()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        Builder.load_file("ui/screens.kv")

        sm = ScreenManager()
        sm.add_widget(IntroScreen(name="intro_screen"))
        sm.add_widget(LoginScreen(name="login_screen"))
        sm.add_widget(SignUpScreen(name="signup_screen"))
        sm.add_widget(UserListScreen(name="user_list_screen"))

        return sm

if __name__ == "__main__":
    MainApp().run()
