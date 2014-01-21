
class AppDataConfigFileGateay(object):
    
    #TODO: Store in os.getenv('APPDATA')
    
    def save_data(self, data):
        raise NotImplementedError("Child Class Must Implement")

    def get_data(self, data):
        raise NotImplementedError("Child Class Must Implement")