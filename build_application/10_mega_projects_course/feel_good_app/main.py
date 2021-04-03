import datetime
import glob
import json
import random
from pathlib import Path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

from kivy.uix.screenmanager import ScreenManager, Screen

from hoverable import HoverBehavior


Builder.load_file('design.kv')


class SignUpScreen(Screen):
    def add_user(self, uname, pswd):
        print(uname, pswd)
        with open("users.json") as file:
            users = json.load(file)
        print(users)
        users[uname] = {
            "username": uname,
            "password": pswd,
            "created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        }
        with open("users.json", 'w') as file:
            json.dump(users, file, indent=2)
        print(users)
        self.manager.current = "sign_up_success"


class SignUpSuccessScreen(Screen):
    def go_to_login_page(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"


class LoginScreen(Screen):
    def sign_up(self):
        print('Sign up button pressed!')
        self.manager.current = "sign_up_screen"

    def login(self, uname, pswd):
        error_msg = ''
        with open("users.json") as file:
            users = json.load(file)
        if uname in users:
            if users[uname]['password'] != pswd:
                error_msg = "username and password does not match."
        else:
            error_msg = "username does not exists."
        if error_msg:
            self.ids.error_msg.text = error_msg
        else:
            self.manager.current = "login_success"


class LoginSuccessScreen(Screen):
    def log_out(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

    def get_quote(self, feeling):
        print(f"feeling selected is {feeling}")
        feel = feeling.lower()
        available_files = glob.glob("quotes/*.txt")
        available_feelings = [Path(fn).stem for fn in available_files]
        if feel in available_feelings:
            with open(f"quotes/{feel}.txt") as file:
                quotes = file.readlines()
            msg = random.choice(quotes)
        else:
            msg = "We don't have quotes for this feeling."
        self.ids.quote.text = msg


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    app = MainApp()
    app.run()
