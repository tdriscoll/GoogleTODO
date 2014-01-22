import json
        
class CorruptConfigFileException(Exception): pass

class BaseConfigFileGateway(object):
    
    DEFAULT_VALUE = json.dumps({})
    
    def save_json(self, data):
        self.save_data(json.dumps(data))

    def get_json(self):
        return json.loads(self.get_data())
        
    def save_data(self, data):
        raise NotImplementedError("Child Class Must Implement")

    def get_data(self):
        raise NotImplementedError("Child Class Must Implement")
    
    def get_value(self, key): 
        try:
            results = self.get_json()
        except ValueError:
            raise CorruptConfigFileException("Not valid JSON in Config")
        if not isinstance(results, dict):
            raise CorruptConfigFileException("Config JSON is not a dict")
        return results.get(key)
    
    def set_values(self, **kwargs):
        data = self.get_json()
        data.update(kwargs)
        self.save_data(json.dumps(data))