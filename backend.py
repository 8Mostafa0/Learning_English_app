import os
from Settings import Settings

class Backend():
    def __init__(self):
        self.set_data()
        self.setting = Settings()

    def set_data(self):
        if not os.path.exists('settings.json'):
            self.set_defualt()
