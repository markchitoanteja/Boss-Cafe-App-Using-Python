import sqlite3
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import hashlib

LOGO_PATH = 'img/logo.png'

def create_db():
    conn = sqlite3.connect('data/user_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        full_name TEXT,
                        username TEXT UNIQUE,
                        password TEXT)''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def check_user_exists(username):
    conn = sqlite3.connect('data/user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def insert_user(full_name, username, password):
    conn = sqlite3.connect('data/user_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (full_name, username, password) VALUES (?, ?, ?)",
                   (full_name, username, password))
    conn.commit()
    conn.close()

def validate_login(username, password):
    conn = sqlite3.connect('data/user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users():
    conn = sqlite3.connect('data/user_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

class IntroScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        scroll_layout = BoxLayout(orientation='vertical', size_hint_y=1)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))
        icon_button = MDIconButton(
            icon="information-outline",
            pos_hint={"center_x": 0.9, "top": 1},
            on_release=self.show_info
        )
        self.add_widget(icon_button)
        logo_box = AnchorLayout(size_hint=(1, None), height="150dp")
        logo = Image(source=LOGO_PATH, size_hint=(None, None), size=(250, 250))
        logo_box.add_widget(logo)
        scroll_layout.add_widget(logo_box)
        welcome_box = AnchorLayout(size_hint=(1, None), height="100dp")
        welcome_label = MDLabel(
            text="Welcome to Boss Cafe App",
            theme_text_color="Secondary",
            halign="center",
            font_style="H4",
            size_hint_y=None,
            height="50dp"
        )
        welcome_box.add_widget(welcome_label)
        scroll_layout.add_widget(welcome_box)
        button_box = AnchorLayout(size_hint=(1, None), height="300dp")
        next_button = MDRaisedButton(
            text="Get Started",
            size_hint=(None, None),
            size=(250, 60),
            on_release=self.go_to_login,
            md_bg_color=self.theme_cls.primary_color,
            pos_hint={"center_x": 0.5},
            elevation=10
        )
        button_box.add_widget(next_button)
        scroll_layout.add_widget(button_box)
        footer_box = AnchorLayout(size_hint=(1, None), height="40dp")
        footer = MDLabel(
            text="\u00A9 2025 Boss Cafe App. All Rights Reserved.",
            theme_text_color="Secondary",
            halign="center"
        )
        footer_box.add_widget(footer)
        scroll_layout.add_widget(footer_box)
        layout.add_widget(scroll_layout)
        self.add_widget(layout)

    def go_to_login(self, instance):
        self.manager.current = "login_screen"

    def show_info(self, instance):
        dialog = MDDialog(
            title="Boss Cafe App",
            text="Application Name: Boss Cafe App\nVersion: 1.0.0\nDescription: A cafe management and ordering app.\nDeveloper: HAIDE MAE G. MERILLO",
            buttons=[
                MDFlatButton(
                    text="OK", on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.on_keyboard)
        layout = AnchorLayout(anchor_y="center", padding=[20, 50])
        container = BoxLayout(orientation="vertical", spacing=20, size_hint=(1, None), height="500dp")
        logo_box = AnchorLayout(size_hint=(1, None), height="120dp")
        logo = Image(source=LOGO_PATH, size_hint=(None, None), size=(200, 200))
        logo_box.add_widget(logo)
        container.add_widget(logo_box)
        title_label = MDLabel(
            text="Login your Account",
            font_style="H5",
            halign="center",
            size_hint=(1, None),
            height="40dp",
            theme_text_color="Primary"
        )
        container.add_widget(title_label)
        form_layout = BoxLayout(orientation="vertical", spacing=20, size_hint=(1, None), height="300dp")
        self.username_field = MDTextField(
            hint_text="Username",
            size_hint=(1, None),
            height="50dp",
            mode="rectangle",
            line_color_normal=self.theme_cls.primary_color,
            line_color_focus=self.theme_cls.primary_color,
        )
        form_layout.add_widget(self.username_field)
        self.password_field = MDTextField(
            hint_text="Password",
            size_hint=(1, None),
            height="50dp",
            mode="rectangle",
            password=True,
            line_color_normal=self.theme_cls.primary_color,
            line_color_focus=self.theme_cls.primary_color,
        )
        form_layout.add_widget(self.password_field)
        login_button = MDRaisedButton(
            text="Login",
            size_hint=(1, None),
            height="50dp",
            on_release=self.login,
            md_bg_color=self.theme_cls.primary_color,
            pos_hint={"center_x": 0.5},
            elevation=10
        )
        form_layout.add_widget(login_button)
        signup_button = MDRaisedButton(
            text="Don't have an account? Sign Up",
            size_hint=(1, None),
            height="50dp",
            on_release=self.go_to_signup,
            md_bg_color=(0.2, 0.6, 0.2, 1),
            pos_hint={"center_x": 0.5},
            elevation=10
        )
        form_layout.add_widget(signup_button)
        container.add_widget(form_layout)
        layout.add_widget(container)
        self.add_widget(layout)

    def on_keyboard(self, window, key, *args):
        if key == 40:
            self.height = Window.height
        return True

    def login(self, instance):
        username = self.username_field.text
        password = self.password_field.text
        user = validate_login(username, password)
        if user:
            self.manager.current = "user_list_screen"
        else:
            dialog = MDDialog(
                title="Login Failed",
                text="Invalid username or password.",
                buttons=[
                    MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())
                ]
            )
            dialog.open()

    def go_to_signup(self, instance):
        self.manager.current = "signup_screen"

class SignUpScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.on_keyboard)
        layout = AnchorLayout(anchor_y="center", padding=[20, 50])
        container = BoxLayout(orientation="vertical", spacing=20, size_hint=(0.9, None), height="550dp")
        logo_box = AnchorLayout(size_hint=(1, None), height="120dp")
        logo = Image(source=LOGO_PATH, size_hint=(None, None), size=(200, 200))
        logo_box.add_widget(logo)
        container.add_widget(logo_box)
        title_label = MDLabel(
            text="Create an Account",
            font_style="H5",
            halign="center",
            size_hint=(1, None),
            height="40dp",
            theme_text_color="Primary"
        )
        container.add_widget(title_label)
        form_layout = BoxLayout(orientation="vertical", spacing=20, size_hint=(1, None), height="400dp")
        self.name_field = MDTextField(
            hint_text="Full Name",
            size_hint=(1, None),
            height="50dp",
            mode="rectangle",
            line_color_normal=self.theme_cls.primary_color,
            line_color_focus=self.theme_cls.primary_color,
        )
        form_layout.add_widget(self.name_field)
        self.username_field = MDTextField(
            hint_text="Username",
            size_hint=(1, None),
            height="50dp",
            mode="rectangle",
            line_color_normal=self.theme_cls.primary_color,
            line_color_focus=self.theme_cls.primary_color,
        )
        form_layout.add_widget(self.username_field)
        self.password_field = MDTextField(
            hint_text="Password",
            size_hint=(1, None),
            height="50dp",
            mode="rectangle",
            password=True,
            line_color_normal=self.theme_cls.primary_color,
            line_color_focus=self.theme_cls.primary_color,
        )
        form_layout.add_widget(self.password_field)
        self.confirm_password_field = MDTextField(
            hint_text="Confirm Password",
            size_hint=(1, None),
            height="50dp",
            mode="rectangle",
            password=True,
            line_color_normal=self.theme_cls.primary_color,
            line_color_focus=self.theme_cls.primary_color,
        )
        form_layout.add_widget(self.confirm_password_field)
        signup_button = MDRaisedButton(
            text="Sign Up",
            size_hint=(1, None),
            height="50dp",
            on_release=self.sign_up,
            md_bg_color=self.theme_cls.primary_color,
            pos_hint={"center_x": 0.5},
            elevation=10
        )
        form_layout.add_widget(signup_button)
        back_to_login_button = MDRaisedButton(
            text="Back to Login",
            size_hint=(1, None),
            height="50dp",
            on_release=self.go_to_login,
            md_bg_color=(0.2, 0.6, 0.2, 1),
            pos_hint={"center_x": 0.5},
            elevation=10
        )
        form_layout.add_widget(back_to_login_button)
        container.add_widget(form_layout)
        layout.add_widget(container)
        self.add_widget(layout)

    def on_keyboard(self, window, key, *args):
        if key == 40:
            self.height = Window.height
        return True

    def sign_up(self, instance):
        full_name = self.name_field.text
        username = self.username_field.text
        password = self.password_field.text
        confirm_password = self.confirm_password_field.text
        if password == confirm_password:
            if check_user_exists(username):
                dialog = MDDialog(
                    title="Sign Up Failed",
                    text="Username already exists.",
                    buttons=[
                        MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())
                    ]
                )
                dialog.open()
            else:
                insert_user(full_name, username, hash_password(password))
                dialog = MDDialog(
                    title="Sign Up Success",
                    text="Account created successfully! You can now log in.",
                    buttons=[
                        MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())
                    ]
                )
                dialog.open()
                self.name_field.text = ""
                self.username_field.text = ""
                self.password_field.text = ""
                self.confirm_password_field.text = ""
        else:
            dialog = MDDialog(
                title="Sign Up Failed",
                text="Passwords do not match.",
                buttons=[
                    MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())
                ]
            )
            dialog.open()

    def go_to_login(self, instance):
        self.manager.current = "login_screen"

class UserListScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10, size_hint=(1, None), height=Window.height)
        logo_box = AnchorLayout(size_hint=(1, None), height="150dp")
        logo = Image(source=LOGO_PATH, size_hint=(None, None), size=(250, 250))
        logo_box.add_widget(logo)
        layout.add_widget(logo_box)
        user_details_layout = BoxLayout(orientation='vertical', size_hint_y=None, height="300dp", spacing=20)
        user_details_layout.pos_hint = {"center_x": 0.5}
        users = get_all_users()
        if users:
            for user in users:
                user_info = f"Full Name: {user[1]}\nUsername: {user[2]}\nPassword (hashed): {user[3]}"
                user_label = MDLabel(
                    text=user_info,
                    theme_text_color="Secondary",
                    halign="center",
                    size_hint_y=None,
                    height="100dp"
                )
                user_details_layout.add_widget(user_label)
        else:
            no_users_label = MDLabel(
                text="No users found.",
                theme_text_color="Secondary",
                halign="center",
                size_hint_y=None,
                height="100dp"
            )
            user_details_layout.add_widget(no_users_label)
        layout.add_widget(user_details_layout)
        logout_button = MDRaisedButton(
            text="Logout",
            size_hint=(1, None),
            height="50dp",
            on_release=self.logout,
            md_bg_color=self.theme_cls.primary_color,
            pos_hint={"center_x": 0.5},
            elevation=10
        )
        layout.add_widget(logout_button)
        self.add_widget(layout)

    def logout(self, instance):
        self.manager.current = "login_screen"

class MyApp(MDApp):
    def build(self):
        create_db()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        screen_manager = Builder.load_string(''' 
ScreenManager:
    IntroScreen:
        name: "intro_screen"
    LoginScreen:
        name: "login_screen"
    SignUpScreen:
        name: "signup_screen"
    UserListScreen:
        name: "user_list_screen"
''')
        return screen_manager

if __name__ == "__main__":
    MyApp().run()
