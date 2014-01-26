import smtplib

class GmailClient(object):
    
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
    
    def send_email(self, email):
        msg = "\r\n".join([
          "From: %s" % email.from_address,
          "To: %s" % email.to_address,
          "Subject: %s" % email.subject,
          "",
          email.body
          ])
        print "emailing..."
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(self.user_name, self.password)
        server.sendmail( email.from_address, email.to_addresses, msg)
        server.quit()
