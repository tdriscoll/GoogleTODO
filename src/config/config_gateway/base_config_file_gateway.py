import json
class ConfigValueNotSetException(Exception):
    
    def __init__(self, field_name):
        self.field_name = field_name
        
class CorruptConfigFileException(Exception): pass


class BaseConfigFileGateway(object):
    
    def save_json(self, data):
        self.save_data(json.dumps(data))

    def get_json(self):
        return json.loads(self.get_data())
        
    def save_data(self, data):
        raise NotImplementedError("Child Class Must Implement")

    def get_data(self, data):
        raise NotImplementedError("Child Class Must Implement")
    
    def get_value(self, key): 
        try:
            results = self.get_json()
        except ValueError:
            raise CorruptConfigFileException("Not valid JSON")
        if not isinstance(results, dict):
            raise CorruptConfigFileException("Value is not a dict")
        if results.has_key(key):
            return results[key]
        raise ConfigValueNotSetException(key)
    
    def set_values(self, **kwargs):
        data = self.get_json()
        data.update(kwargs)
        self.save_data(json.dumps(data))