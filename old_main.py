# orginal old main.py
# has firebase code

# IMPORTS
## KivyMD
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.toast import toast              # toast_pop_up(StudyBudApp)
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from kivy.uix.boxlayout import BoxLayout

## Kivy
#from kivy.lang import Builder
## Pyrebase4
#import pyrebase
#from pyrebase import firebaseConfig
## Local Imports
#import firebaseloginscreen

# REQUIRE
#kivymd.require(104.2)

# FIREBASE CONNECTION
#firebaseConif = {'apiKey': "AIzaSyBI-WHUvB3Fy7Ypj5sTyVQF5Y_H66iJ5Rs",
#                 'authDomain': "meghaventurestudybud.firebaseapp.com",
#                 'projectId': "meghaventurestudybud",
#                 'storageBucket': "meghaventurestudybud.appspot.com",
#                 'messagingSenderId': "187515988154",
#                 'appId': "1:187515988154:web:55b8a3f7e002b2940b3a83",
#                 'measurementId': "G-RRV8FLV4KV"
#                 }
#firebase = pyrebase.initialize_app(firebaseConfig)

#db = firebase.database()
#auth = firebase.auth()
#storage = firebase.storage()


#def callback(text_of_selection: str, popup_widget: str):
#    text_input = popup_widget.text_field.text
#    selection = text_of_selection
#    return text_input, selection


#def open_theme_picker():
#    theme_picker = MDThemePicker()
#    theme_picker.open()


class StudyBudApp(MDApp):
#    theme_cls = ThemeManager()
    def __init__(self, **kwargs):
        super(StudyBudApp, self).__init__(**kwargs) #todo find error
        ## THEME
#        theme_cls.theme_style = "Dark"
#        theme_cls.primary_palette = "Purple"
#        theme_cls.accent_palette = "Green"
#        theme_cls.accent_hue = 400  # gives accent color a hue value
#        self.input_alert_pop_up_hint = None
#        self.input_alert_pop_up_title = None
#        self.toast_pop_up_message = None
#        self.alert_pop_up_title = None
#        self.alert_pop_up_message = None

#    def on_start(self):
 #       pass

#    def build(self):
#        pass


        ## POP UP MESSAGES
 #   def toast_pop_up(self, message: str):
 #       self.toast_pop_up_message = message
 #       toast("message")

    ### ALERT
 #   def alert_pop_up(self, title: str, message: str):
 #       self.alert_pop_up_title = title
  #      self.alert_pop_up_message = message
  #      alert = MDDialog(title=self.alert_pop_up_title,
 #                        text=self.alert_pop_up_message,
  #                       size_hint=[.5, .5],
  #                       auto_dismiss=False,
  #                       events_callback=callback,
  #                       text_button_ok="I agree",
  #                       text_button_cancel="I don't agree")
  #      alert.open()

    ### INPUT
 #   def input_alert_pop_up(self, title: str, hint: str):
 #       self.input_alert_pop_up_title = title
 #       self.input_alert_pop_up_hint = hint
 #       alert = MDDialog(title=self.input_alert_pop_up_title,
  #                       hint_text=self.input_alert_pop_up_hint,
  #                       size_hint=[.5, .5],
  #                       auto_dismiss=False,
  #                       events_callback=callback,
  #                       text_button_ok="Submit",
  #                       text_button_cancel="Cancel")
  #      alert.open()

    ## PICKERS
    ### DATE PICKER
 #   def open_date_picker(self):
 #       date_picker = MDDatePicker(callback=self.save_date)
 #       date_picker.open()

 #   def save_date(self, selected_date):
  #      self.year = selected_date.year
  #      self.month = selected_date.month
   #     self.day = selected_date.day

    ### TIME PICKER
    #def open_time_picker(self):
    #    time_picker = MDTimepicker()
    #    time_picker.bind(time=self.save_time)
    #    time_picker.open()

 #   def save_time(self, picker_widget: str, time):
 #       self.hour = time.hour
 #       self.minute = time.minute
 #       self.second = time.second

    ### THEME PICKER

    ### AUTO LOGIN???
    #def on_start(self):
    #    Clock.schedule_once(self, login, password)


# USERS
#class User:
 #   def __init__(self, names: [], pronouns: [], birthday: str, email: str, password: str, user_id: str):
 #       self.names = names
 #       self.pronouns = pronouns
 #       self.birthday = birthday
 #       self.email = email
 #       self.user_id = user_id

    #def __repr__(self):
    #    return f"Preferred Names: {names}; Pronouns: {pronouns}; Birthday: {birthday}; E - mail: {email}; User ID: {user_id}."


# RUN
if __name__ == '__main__':  # use when only want to run as main (not import)
    StudyBudApp().run()
