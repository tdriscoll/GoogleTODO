from base64 import b64encode, b64decode

class EmailNotSetException(Exception): pass
class PasswordNotSetException(Exception): pass

class Configuration(object):
    
    gateway = None
    
    @classmethod
    def get_email_address(cls):
        email = cls.gateway.get_value('email_address')
        if not email:
            raise EmailNotSetException()
        return email

    @classmethod
    def get_password(cls):
        encoded_password = cls.gateway.get_value('password')
        if not encoded_password:
            raise PasswordNotSetException()
        return b64decode(encoded_password)
    
    @classmethod
    def set_email_address(cls, email_address):
        return cls.gateway.set_values(email_address = email_address)

    @classmethod
    def set_password(cls, password):
        return cls.gateway.set_values(password = b64encode(password))
    

