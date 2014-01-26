from config.config_file_gateway.base import BaseConfigFileGateway
from os.path import isfile, expanduser

class HomeDirectoryConfigFileGateway(BaseConfigFileGateway):
    
    def __init__(self, program_name):
        home_dir = expanduser('~')
        self.FILE_PATH = '{home_dir}/.{program_name}'.format(home_dir=home_dir, program_name = program_name)
    
    def save_data(self, data):
        try:
            with open(self.FILE_PATH, 'w') as f:
                f.write(data)
        except IOError:
            raise
            raise Exception("Not able to write to '%s' (no permissions?)" % self.FILE_PATH)

    def get_data(self):
        if not isfile(self.FILE_PATH):
            return self.DEFAULT_VALUE
        with open(self.FILE_PATH, 'r') as f:
            return f.read()