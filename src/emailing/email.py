from common.domain_object import DomainObject

class BadUsernamePasswordException(Exception): pass

class EmailFromMyself(DomainObject):
    
    def __init__(self, subject, body, to_address):
        self.subject = subject
        self.body = body
        self.to_address = to_address
        
    @property
    def from_address(self):
        return self.to_address
    
    @property
    def to_addresses(self):
        return [self.to_address]
