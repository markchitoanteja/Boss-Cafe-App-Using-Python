import sqlite3
import kivy
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

kivy.require('2.0.0')

# Set the window size to mimic a mobile phone screen size
Window.size = (360, 640)  # Typical mobile phone screen size in pixels (360x640)

# SQLite database setup
def create_db():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        uuid TEXT UNIQUE,
                        name TEXT,
                        username TEXT UNIQUE,
                        password TEXT,
                        created_at TEXT,
                        updated_at TEXT
                    )''')
    conn.commit()
    conn.close()

# Intro Screen
class IntroScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        logo = Image(source='logo.png', size_hint=(None, None), size=(150, 150), pos_hint={'center_x': 0.5})
        layout.add_widget(logo)

        layout.add_widget(MDLabel(text="Welcome to Boss Cafe", halign="center", theme_text_color="Primary", font_style="H5"))

        start_button = MDRaisedButton(text="Get Started", size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        start_button.bind(on_press=self.on_get_started)
        layout.add_widget(start_button)

        layout.add_widget(MDLabel(text="© 2025 Boss Cafe, All rights reserved", halign="center", theme_text_color="Hint"))

        self.add_widget(layout)

    def on_get_started(self, instance):
        self.manager.current = "login"

# Login Screen
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        logo = Image(source='logo.png', size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        layout.add_widget(logo)

        card = MDCard(size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.5})
        card_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        card_layout.add_widget(MDLabel(text="Login", theme_text_color="Secondary", halign="center", font_style="H6"))
        card_layout.add_widget(MDTextField(hint_text="Username"))
        card_layout.add_widget(MDTextField(hint_text="Password", password=True))

        # Buttons in one row, each covering 50% of the card width
        button_container = BoxLayout(orientation="horizontal", spacing=10, size_hint=(1, None), height=50)
        
        login_button = MDRaisedButton(text="Login", md_bg_color=(0, 0.6, 1, 1), size_hint_x=0.5)  # Blue
        signup_button = MDRaisedButton(text="Sign Up", md_bg_color=(0.16, 0.73, 0.28, 1), size_hint_x=0.5)  # Green
        signup_button.bind(on_press=self.go_to_signup)

        button_container.add_widget(login_button)
        button_container.add_widget(signup_button)

        card_layout.add_widget(button_container)
        card.add_widget(card_layout)
        layout.add_widget(card)

        layout.add_widget(MDLabel(text="© 2025 Boss Cafe, All rights reserved", halign="center", theme_text_color="Hint"))

        self.add_widget(layout)

    def go_to_signup(self, instance):
        self.manager.current = "signup"

# Signup Screen
class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        logo = Image(source='logo.png', size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5})
        layout.add_widget(logo)

        card = MDCard(size_hint=(None, None), size=(300, 350), pos_hint={'center_x': 0.5})
        card_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        card_layout.add_widget(MDLabel(text="Sign Up", theme_text_color="Secondary", halign="center", font_style="H6"))
        card_layout.add_widget(MDTextField(hint_text="Name"))
        card_layout.add_widget(MDTextField(hint_text="Username"))
        card_layout.add_widget(MDTextField(hint_text="Password", password=True))

        # Buttons in one row, each covering 50% of the card width
        button_container = BoxLayout(orientation="horizontal", spacing=10, size_hint=(1, None), height=50)
        
        signup_button = MDRaisedButton(text="Sign Up", md_bg_color=(0, 0.6, 1, 1), size_hint_x=0.5)  # Blue
        signin_button = MDRaisedButton(text="Sign In", md_bg_color=(0.16, 0.73, 0.28, 1), size_hint_x=0.5)  # Green
        signin_button.bind(on_press=self.go_to_login)

        button_container.add_widget(signup_button)
        button_container.add_widget(signin_button)

        card_layout.add_widget(button_container)
        card.add_widget(card_layout)
        layout.add_widget(card)

        layout.add_widget(MDLabel(text="© 2025 Boss Cafe, All rights reserved", halign="center", theme_text_color="Hint"))

        self.add_widget(layout)

    def go_to_login(self, instance):
        self.manager.current = "login"

# KivyMD App
class MyApp(MDApp):
    def build(self):
        # Set the app's theme to Dark Mode by default
        self.theme_cls.theme_style = "Dark"
        
        sm = ScreenManager()
        sm.add_widget(IntroScreen(name="intro"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(SignupScreen(name="signup"))
        
        return sm

if __name__ == '__main__':
    create_db()
    MyApp().run()
