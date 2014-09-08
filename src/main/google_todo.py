#!/usr/bin/env python
# encoding: utf-8
''' See the README.md '''

import sys
import os
from emailing.task_mailer import TaskMailer, MissingTaskException
from config.configuration import Configuration, EmailNotSetException,\
    PasswordNotSetException
from config.config_file_gateway.app_data import AppDataConfigFileGateway
from config.config_file_gateway.home_directory import HomeDirectoryConfigFileGateway
from emailing.email_client.gmail import GmailClient
from config.config_file_gateway.base import CorruptConfigFileException
from emailing.email import BadUsernamePasswordException

PROGRAM_NAME = "google_todo"
if os.name == 'nt':
    Configuration.gateway = AppDataConfigFileGateway(PROGRAM_NAME)
else:
    Configuration.gateway = HomeDirectoryConfigFileGateway(PROGRAM_NAME)

def main():
    while True:
        try:
            email_client = GmailClient(Configuration.get_email_address(), Configuration.get_password())
            task = raw_input("What task? ")
            TaskMailer(task=task, email_client=email_client).send()
            print  "Task sent successfully!"
        except MissingTaskException:
            print "Seriously we need a task..."
        except EmailNotSetException:
            Configuration.set_email_address(raw_input("We need your GMail username.  What is it? "))
        except PasswordNotSetException:
            Configuration.set_password(raw_input("We need your GMail password.  Give it up! "))
        except BadUsernamePasswordException:
            Configuration.set_password(raw_input("Google said your password was garbage. Want to try a new one? "))
        except CorruptConfigFileException:
            sys.stderr.write("Your config is corrupt.  Why don't you fix it? ")
            return
        #TODO: handle no internets
            
if __name__ == "__main__":
    sys.exit(main())
