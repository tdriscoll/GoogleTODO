from config.config_gateway.base_config_file_gateway import BaseConfigFileGateway

class InMemoryConfigFileGateway(BaseConfigFileGateway):
    
    def __init__(self):
        self.save_json({})
    
    def get_data(self):
        return self.data
    
    def save_data(self, data):
        self.data = data