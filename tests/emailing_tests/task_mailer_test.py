import unittest
from emailing.task_mailer import TaskMailer, MissingTaskException
from emailing.email import Email
from in_memory.email_client import InMemoryEmailClient
from config.configuration import Configuration
from config.config_gateway.in_memory import InMemoryConfigFileGateway

class EmailCreatorTest(unittest.TestCase):
    
    def setUp(self):
        Configuration.gateway = InMemoryConfigFileGateway()
        Configuration.set_email_address('bob@mailme.com')
    
    def test_raise_exception_when_no_task(self):
        self.assertRaises(MissingTaskException, TaskMailer(task="").send)

    def test_given_a_task_can_email_it(self):
        task_mailer = TaskMailer(task="Get this test passing")
        task_mailer.email_client = InMemoryEmailClient()
        task_mailer.send()
        self.assertEqual([Email(subject="TODO: Get this test passing", body="from GoogleTODO", to_addresses=['bob@mailme.com'])], task_mailer.email_client.sent_mail)
        
