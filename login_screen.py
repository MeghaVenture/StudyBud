# login_screen.py

# IMPORTS
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('screens/login_screen.kv')

class LogIn_Screen(Screen):
    def validate_user(self):
        Username = self.ids.Username.txt
        if Username in list(details.keys()):
            if details[Usernane] == self.ids.Pawword.tx:
                MDApp.get_running_app().switch_screen(home_screen)
            else:
                pass
