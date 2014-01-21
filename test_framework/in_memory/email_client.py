class InMemoryEmailClient(object):
    
    def __init__(self):
        self.sent_mail = []

    def send_email(self, email):
        self.sent_mail.append(email)