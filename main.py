# main.py - the main py file for the app

# IMPORTS
## kivy
from kivy.properties import ObjectProperty
## KivyMD - issues! very finicky & big changes !
from kivymd.app import MDApp
from kivymd.uix.navigationdrawer import MDNavigationDrawer
#from kivymd.uix.toolbar import MDTopAppBar # IMPORT ERROR - no answers in documentation
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
# consider MDSliverAppBar (new, uses MDTopAppBar - fix issues?) - docs are lacking
## LOCAL IMPORTS
### SCREENS
from screens.home_screen import Home_Screen
from screens.login_screen import LogIn_Screen
from screens.signup_screen import SignUp_Screen
from screens.tools_screen import Tools_Screen
from screens.msg_notif_screen import Msg_Notif_Screen
from screens.grades_stats_screen import Grades_Stats_Screen
from screens.cal_todo_screen import Cal_ToDo_Screen
from screens.collections_screen import Collections_Screen
from screens.game_screen import Game_Screen
from screens.setting_screen import Setting_Screen
from screens.trophies_screen import Trophies_Screen
from screens.file_manager_screen import File_Manager_Screen

# REQUIREMENTS - add "requirements.txt"

# SCREEN MANAGER - rest see "BUILD"
class Screen_Manager(MDScreenManager):
    pass

# ROOT SCREEN
class RootScreen(MDScreen):
    screen_manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ## create an instance of the Screen_Manager class to use
        self.screen_manager = Screen_Manager()
        ## add screens to the screen_manger
        self.screen_manager.add_widget(Home_Screen(name="Home_Screen"))
        self.screen_manager.add_widget(LogIn_Screen(name="LogIn_Screen"))
        self.screen_manager.add_widget(SignUp_Screen(name="SignUp_Screen"))
        self.screen_manager.add_widget(Tools_Screen(name="Tools_Screen"))
        self.screen_manager.add_widget(Msg_Notif_Screen(name="Msg_Notif_Screen"))
        self.screen_manager.add_widget(Grades_Stats_Screen(name="Grades_Stats_Screen"))
        self.screen_manager.add_widget(Cal_ToDo_Screen(name="Cal_ToDo_Screen"))
        self.screen_manager.add_widget(Collections_Screen(name="Collections_Screen"))
        self.screen_manager.add_widget(Game_Screen(name="Game_Screen"))
        self.screen_manager.add_widget(Setting_Screen(name="Setting_Screen"))
        self.screen_manager.add_widget(Trophies_Screen(name="Trophies_Screen"))
        self.screen_manager.add_widget(File_Manager_Screen(name="File_Manager_Screen"))


# MAIN APP
class StudyBudApp(MDApp):
    def build(self):
        '''Creates the app and returns the Root Screen'''
        '''
        Color Options: Red, Pink, Purple, DeepPurple,
                Indigo, Blue, LightBlue, Cyan, Teal, Green,
                LightGreen, Lime, Yellow, Amber, Orange, DeepOrange,
                Brown, Gray, and BlueGray
        '''
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Purple"
        self.theme_cls.accent_hue = "400"
        # Create the root widget
        root = RootScreen()
        nav_drawer = MDNavigationDrawer()
        root.add_widget(nav_drawer)
        # Add the toolbar and screen manager to the root widget
        root.add_widget(MDTopAppBar())
        root.add_widget(self.root.screen_manager)
        # Set the opening window to the LogIn_Screen
        self.root.screen_manager.current = "LogIn_Screen"
        return root
    #   Builder.load_string("studybud.kv")


if __name__ == "__main__":
    StudyBudApp().run()
