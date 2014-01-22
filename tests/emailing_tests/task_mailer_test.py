import unittest
from emailing.task_mailer import TaskMailer, MissingTaskException
from config.configuration import Configuration
from config.config_file_gateway.in_memory import InMemoryConfigFileGateway
from emailing.email import EmailFromMyself
from emailing.email_client.in_memory import InMemoryEmailClient

class EmailCreatorTest(unittest.TestCase):
    
    def setUp(self):
        Configuration.gateway = InMemoryConfigFileGateway()
        Configuration.set_email_address('bob@mailme.com')
    
    def test_raise_exception_when_no_task(self):
        self.assertRaises(MissingTaskException, TaskMailer(task="", email_client=InMemoryEmailClient()).send)

    def test_given_a_task_can_email_it(self):
        task_mailer = TaskMailer(task="Get this test passing", email_client = InMemoryEmailClient())
        task_mailer.send()
        self.assertEqual([EmailFromMyself(subject="TODO: Get this test passing", body="from GoogleTODO", to_address='bob@mailme.com')], task_mailer.email_client.sent_mail)    
