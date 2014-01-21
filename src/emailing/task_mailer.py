from emailing.email import Email
from config.configuration import Configuration

class MissingTaskException(Exception): pass

class TaskMailer(object):

    email_client = None
    
    def __init__(self, task):
        self.task = task
    
    def send(self):
        if not self.task:
            raise MissingTaskException()
        self.email_client.send_email(Email(subject="TODO: {task}".format(task=self.task), body="from GoogleTODO", to_addresses=[Configuration.get_email_address()]))