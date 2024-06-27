import json
from logger import logger
class Settings:
    def __init__(self, filename='settings.json'):
        self.filename = filename
        self.logg = logger()
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}
            self.save()

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.logg.log(f"Setting :{key} Set To {value}")
        self.data[key] = value
        self.save()

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def light_theme(self):
        self.logg.log("Theme Set To Light")
        self.set('theme', 30)
        self.set('main_color', 'John Doe')
        self.set('fr_color', 30)
        self.set('bg_color', 30)
        self.set('sec_color', 30)
        self.set('prim_color', 30)
        self.set('bt_color', 30)
        self.set('ac_bt_color', 30)
        self.set('hv_bt_color', 30)
    
    def dark_theme(self):
        self.logg.log("Theme Set To Dark")
        self.set('theme', 30)
        self.set('main_color', 'John Doe')
        self.set('fr_color', 30)
        self.set('bg_color', 30)
        self.set('sec_color', 30)
        self.set('prim_color', 30)
        self.set('bt_color', 30)
        self.set('ac_bt_color', 30)
        self.set('hv_bt_color', 30)
    
    def user_logged(self,log):
        self.save("user_logged_in",log)

    def logg_user(self,username,password):
        self.logg.log("User Loged In")
        self.set('username', username)
        self.set('password', password)
        self.user_logged(False)


    def set_defualt(self):
        self.logg.log("Setting Set To Defualt")
        self.light_theme()
        self.set('last_score', 30)
        self.set('user_token', 30)
        self.set('last_book', 30)
        self.set('last_lessen', 30)
        self.set('last_l_mode', 30)
        self.set('last_item', 30)