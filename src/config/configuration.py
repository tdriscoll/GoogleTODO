from base64 import b64encode, b64decode

class Configuration(object):
    
    gateway = None
    
    @classmethod
    def get_email_address(cls):
        return cls.gateway.get_value('email_address')

    @classmethod
    def get_password(cls):
        return b64decode(cls.gateway.get_value('password'))
    
    @classmethod
    def set_email_address(cls, email_address):
        return cls.gateway.set_values(email_address = email_address)

    @classmethod
    def set_password(cls, password):
        return cls.gateway.set_values(password = b64encode(password))
    

