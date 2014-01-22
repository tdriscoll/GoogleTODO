from config.config_file_gateway.base import BaseConfigFileGateway

class InMemoryConfigFileGateway(BaseConfigFileGateway):
    
    def __init__(self):
        self.data = self.DEFAULT_VALUE
    
    def get_data(self):
        return self.data
    
    def save_data(self, data):
        self.data = data