from common.domain_object import DomainObject

class Email(DomainObject):
    
    def __init__(self, subject, body, to_addresses):
        self.subject = subject
        self.body = body
        self.to_addresses = to_addresses