class InMemoryEmailClient(object):
    """ Doesn't actually send the emails since they just live in memory. :( """
    
    def __init__(self):
        self.sent_mail = []

    def send_email(self, email):
        self.sent_mail.append(email)