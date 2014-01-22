from config.config_file_gateway.base import BaseConfigFileGateway

class HomeDirectoryConfigFileGateway(BaseConfigFileGateway):
    
    #TODO: Store in  ~/.googleTODO
    
    def save_data(self, data):
        raise NotImplementedError("Child Class Must Implement")

    def get_data(self):
        raise NotImplementedError("Child Class Must Implement")