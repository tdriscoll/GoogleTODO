import unittest
from emailing.email import EmailFromMyself


class EmailTest(unittest.TestCase):
    
    def test_an_email_from_myself_has_enough_data_to_email(self):
        email = EmailFromMyself(subject="free money", body="just wire transfer me money first", to_address="sucker@hotmail.com")
        self.assertEquals(["sucker@hotmail.com"], email.to_addresses)
        self.assertEquals("sucker@hotmail.com", email.from_address)
    
