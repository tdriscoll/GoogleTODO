import unittest
from email.email_creator import MissingTaskException, EmailCreator


class EmailCreatorTest(unittest.TestCase):


    def test_raise_exception_when_no_task(self):
        self.assertRaises(MissingTaskException, EmailCreator(task="").run)


