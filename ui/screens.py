from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from backend.auth import sign_up_user, login_user, logout_user

class IntroScreen(MDScreen):
    def go_to_login(self, instance):
        self.manager.current = "login_screen"

    def show_info(self, instance):
        dialog = MDDialog(
            title="Boss Cafe App",
            text="Application Name: Boss Cafe App\nVersion: 1.0.0\nDescription: A cafe management and ordering app.\nDeveloper: HAIDE MAE G. MERILLO",
            buttons=[MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()

class SignUpScreen(MDScreen):
    def on_keyboard(self, _, key, *args):
        if key == 40:
            self.height = Window.height
        return True

    def sign_up(self, _):
        full_name = self.ids.name_field.text
        email = self.ids.email_field.text  # <-- New
        username = self.ids.username_field.text
        password = self.ids.password_field.text
        confirm_password = self.ids.confirm_password_field.text

        success, message = sign_up_user(full_name, email, username, password, confirm_password)
        
        dialog = MDDialog(
            title="Sign Up" if success else "Sign Up Failed",
            text=message,
            buttons=[MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())]
        )
        dialog.open()
        if success:
            self.manager.current = "login_screen"

    def go_to_login(self, _):
        self.manager.current = "login_screen"

class LoginScreen(MDScreen):
    def on_keyboard(self, window, key, *args):
        if key == 40:
            self.height = Window.height
        return True

    def login(self):
        username = self.ids.username_field.text
        password = self.ids.password_field.text
        success, result = login_user(username, password)
        
        if success:
            # Assuming result is a tuple (user_id, full_name)
            user_id, full_name = result
            self.manager.get_screen("user_list_screen").current_user_full_name = full_name
            self.manager.get_screen("user_list_screen").current_user_id = user_id  # Store the user ID
            self.manager.current = "user_list_screen"
        else:
            dialog = MDDialog(
                title="Login Failed",
                text=result,
                buttons=[MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())]
            )
            dialog.open()


    def go_to_signup(self, instance):
        self.manager.current = "signup_screen"

class UserListScreen(MDScreen):
    current_user_full_name = ""
    current_user_id = None  # This will hold the current user's ID
    
    # This method runs before entering the screen, sets the welcome label.
    def on_pre_enter(self):
        if self.ids.welcome_label:
            self.ids.welcome_label.text = f"Welcome, {self.current_user_full_name}!"
    
    # The logout function that gets called when the logout button is pressed
    def logout(self, instance):
        # Check if current_user_id is set
        if self.current_user_id:
            # Optionally log out the user (e.g., logging the session to a database)
            logout_user(self.current_user_id)  # Ensure logout_user is implemented if needed

        # Navigate to the login screen
        self.manager.current = "login_screen"
