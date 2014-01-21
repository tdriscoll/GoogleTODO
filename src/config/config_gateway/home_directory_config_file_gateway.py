
class HomeDirectoryConfigFileGateay(object):
    
    #TODO: Store in  ~/.googleTODO
    
    def save_data(self, data):
        raise NotImplementedError("Child Class Must Implement")

    def get_data(self, data):
        raise NotImplementedError("Child Class Must Implement")