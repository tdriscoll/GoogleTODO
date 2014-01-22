from os import getenv, makedirs
from os.path import join, exists, isfile
from config.config_file_gateway.base import BaseConfigFileGateway

class AppDataConfigFileGateway(BaseConfigFileGateway):
    
    def __init__(self, program_name):
        self.DIR_PATH = join(getenv('APPDATA'), program_name) 
        self.FILE_PATH = join(self.DIR_PATH, 'config.json')
    
    def save_data(self, data):
        if not exists(self.DIR_PATH):
            makedirs(self.DIR_PATH)
        with open(self.FILE_PATH, 'w') as f:
            f.write(data)

    def get_data(self):
        if not isfile(self.FILE_PATH):
            return self.DEFAULT_VALUE
        with open(self.FILE_PATH, 'r') as f:
            return f.read()
        
