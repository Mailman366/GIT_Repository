############################################################################################
#
# Description
#   - Common email module
#
#
#
#
#############################################################################################

import os
import smtplib
from email.mime.text import MIMEText
from ConfigParser import RawConfigParser
from email.mime.multipart import MIMEMultipart

CONFIG_FILE = 'config.ini'
PARENT_PATH = os.path.abspath(os.path.join(__file__ ,"../.."))
CONFIG_PATH = os.path.join(PARENT_PATH, CONFIG_FILE)


# Exceptions
class EmailException(Exception):
    pass


class EmailWriter(object):

    TO = "To"
    FROM = "From"
    SUBJECT = "Subject"
    BODY = "Body"
    REQUIRED_KEYS = [TO, SUBJECT, BODY]

    def __init__(self, email_dict):
        self.email_dict = email_dict
        self.from_address, self.from_pw = self.read_config()

    def verify_dict(self):

        # Ensure Types
        if not isinstance(self.email_dict, dict):
            raise EmailException("EmailWriter requires a dictionary!")

        # Ensure dictionary
        missing_keys = [k for k in self.REQUIRED_KEYS if k not in self.email_dict.keys()]
        if missing_keys:
            raise EmailException("Missing the following email keys: {0}".format(missing_keys))

        return True

    def write_email(self):
        # Verify that proper parameters are provided
        self.verify_dict()

        # Construct email
        msg = MIMEMultipart()
        msg['From'] = self.from_address
        msg['To'] = self.email_dict['To']
        msg['Subject'] = self.email_dict['Subject']

        body = self.email_dict['Body']
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.from_address, self.from_pw)
        text = msg.as_string()
        print("Attempting to send an email to {}..".format(msg["To"]))
        server.sendmail(self.from_address, self.email_dict['To'], text)
        print("Successfully sent email to {}!".format(msg["To"]))
        server.quit()

    def read_config(self):
        """Reads a config file to obtain email credentials"""

        # Verify config file exists
        if not os.path.exists(CONFIG_PATH):
            raise IOError("Unable to find config.ini!")

        config = RawConfigParser()
        config.read(CONFIG_PATH)
        return (config.get('CREDENTIALS', 'username'),  config.get('CREDENTIALS', 'password'))
