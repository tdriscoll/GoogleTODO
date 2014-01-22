from emailing.email import EmailFromMyself
from config.configuration import Configuration

class MissingTaskException(Exception): pass

class TaskMailer(object):

    def __init__(self, task, email_client):
        self.task = task
        self.email_client = email_client
    
    def send(self):
        if not self.task:
            raise MissingTaskException()
        self.email_client.send_email(EmailFromMyself(subject="TODO: {task}".format(task=self.task),
                                                     body="from GoogleTODO",
                                                     to_address=Configuration.get_email_address()))
