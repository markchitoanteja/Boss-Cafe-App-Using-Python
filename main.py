from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image


# Define the path for the logo image
LOGO_PATH = 'assets/img/logo.png'


class IntroScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create layout for the intro screen
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Create a scrollable layout for the content
        scroll_layout = BoxLayout(orientation='vertical', size_hint_y=1)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))

        # Logo container
        logo_box = AnchorLayout(size_hint=(1, None), height="150dp")
        logo = Image(source=LOGO_PATH, size_hint=(None, None), size=(250, 250))
        logo_box.add_widget(logo)
        scroll_layout.add_widget(logo_box)

        # Welcome message container
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

        # Button container
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

        # Footer
        footer_box = AnchorLayout(size_hint=(1, None), height="40dp")
        footer = MDLabel(
            text="© 2025 Boss Cafe App. All Rights Reserved.",
            theme_text_color="Secondary",
            halign="center"
        )
        footer_box.add_widget(footer)
        scroll_layout.add_widget(footer_box)

        # Adding the scrollable layout to the main layout
        layout.add_widget(scroll_layout)
        self.add_widget(layout)

    def go_to_login(self, instance):
        # Move to the login screen after "Get Started" button is clicked
        self.manager.current = "login_screen"


class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create layout for the login screen
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Create a logo container
        logo_box = AnchorLayout(size_hint=(1, None), height="150dp")
        logo = Image(source=LOGO_PATH, size_hint=(None, None), size=(200, 200))
        logo_box.add_widget(logo)
        layout.add_widget(logo_box)

        # Create a container for the form
        form_layout = BoxLayout(orientation='vertical', spacing=20, size_hint_y=None, height="300dp")
        form_layout.padding = [30, 0, 30, 0]  # Add padding to the form layout

        # Username field
        self.username_field = MDTextField(
            hint_text="Username",
            size_hint=(1, None),
            height="50dp",
            mode="rectangle",
            line_color_normal=self.theme_cls.primary_color,
            line_color_focus=self.theme_cls.primary_color,
        )
        form_layout.add_widget(self.username_field)

        # Password field
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

        # Login button
        login_button = MDRaisedButton(
            text="Login",
            size_hint=(None, None),
            size=(250, 60),
            on_release=self.login,
            md_bg_color=self.theme_cls.primary_color,
            pos_hint={"center_x": 0.5},
            elevation=10
        )
        form_layout.add_widget(login_button)

        # Add form layout to the main layout
        layout.add_widget(form_layout)

        # Add clickable Sign Up link
        signup_link = MDLabel(
            text="Don't have an account? Sign Up",
            theme_text_color="Primary",  # Changed to make it more visible
            halign="center",
            on_release=self.go_to_signup,
            markup=True,  # To allow the clickable action
            size_hint=(None, None),
            height="40dp"
        )
        layout.add_widget(signup_link)

        # Add the layout to the screen
        self.add_widget(layout)

    def login(self, instance):
        # Logic for handling login
        username = self.username_field.text
        password = self.password_field.text
        print(f"Logging in with Username: {username} and Password: {password}")
        # Add validation and authentication logic here

    def go_to_signup(self, instance):
        # Logic for transitioning to Sign Up screen
        self.manager.current = "signup_screen"


class SignUpScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create layout for the sign-up screen
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Create a logo container
        logo_box = AnchorLayout(size_hint=(1, None), height="150dp")
        logo = Image(source=LOGO_PATH, size_hint=(None, None), size=(200, 200))
        logo_box.add_widget(logo)
        layout.add_widget(logo_box)

        # Create a container for the form
        form_layout = BoxLayout(orientation='vertical', spacing=20, size_hint_y=None, height="400dp")
        form_layout.padding = [30, 0, 30, 0]  # Add padding to the form layout

        # Name field
        self.name_field = MDTextField(
            hint_text="Full Name",
            size_hint=(1, None),
            height="50dp",
            mode="rectangle",
            line_color_normal=self.theme_cls.primary_color,
            line_color_focus=self.theme_cls.primary_color,
        )
        form_layout.add_widget(self.name_field)

        # Username field
        self.username_field = MDTextField(
            hint_text="Username",
            size_hint=(1, None),
            height="50dp",
            mode="rectangle",
            line_color_normal=self.theme_cls.primary_color,
            line_color_focus=self.theme_cls.primary_color,
        )
        form_layout.add_widget(self.username_field)

        # Password field
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

        # Confirm Password field
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

        # Sign Up button
        signup_button = MDRaisedButton(
            text="Sign Up",
            size_hint=(None, None),
            size=(250, 60),
            on_release=self.sign_up,
            md_bg_color=self.theme_cls.primary_color,
            pos_hint={"center_x": 0.5},
            elevation=10
        )
        form_layout.add_widget(signup_button)

        # Add form layout to the main layout
        layout.add_widget(form_layout)

        # Add the layout to the screen
        self.add_widget(layout)

    def sign_up(self, instance):
        # Logic for handling sign up
        name = self.name_field.text
        username = self.username_field.text
        password = self.password_field.text
        confirm_password = self.confirm_password_field.text

        if password == confirm_password:
            print(f"Signing up with Name: {name}, Username: {username}")
            # Add sign up logic here (e.g., saving to database)
        else:
            print("Passwords do not match!")

class MyApp(MDApp):
    def build(self):
        # Enable dark mode by setting the theme style to 'Dark'
        self.theme_cls.theme_style = "Dark"
        
        # Optional: Change primary color if needed
        self.theme_cls.primary_palette = "Blue"

        # Screen manager to manage the pages
        screen_manager = Builder.load_string('''
ScreenManager:
    IntroScreen:
        name: "intro_screen"
    LoginScreen:
        name: "login_screen"
    SignUpScreen:
        name: "signup_screen"
''')

        return screen_manager


if __name__ == "__main__":
    MyApp().run()
