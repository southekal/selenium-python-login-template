__author__ = 'Southekal'

from helpers import driverutil
from helpers import locators
import time
import ConfigParser

"""config settings"""
config = ConfigParser.RawConfigParser()
config.read('./default.cfg')


class CreateUserElements(object):

    def __init__(self):
        self.browser = driverutil.WebDriver()
        self.browser.setUp()
        self.login_page = locators.SignUpPageLocators()
        self.link = self.login_page.SIGNUP_URL
        self.name_id = self.login_page.NAME_ID
        self.email_class = self.login_page.EMAIL_CLASS
        self.create_class = self.login_page.CREATE_CLASS
        self.name = config.get('SignUp', 'name')
        self.email = config.get('SignUp', 'email')
        self.error_msg = self.login_page.ERROR_MSG_CLASS

    def tear_down(self):
        self.browser.tearDown()

    def enter_sign_up_details(self):
        """
        Enters sign in details
        """
        name_elem = self.browser.get_id(self.name_id)[0]
        time.sleep(3)  # delays for 3 seconds
        name_elem.send_keys(self.name)
        email_elem = self.browser.get_class(self.email_class)[0]
        email_elem.send_keys(self.email)
        self.browser.get_class(self.create_class)[0].click()

        if len(self.browser.get_class(self.error_msg)) > 0:
            print '[INFO]: Check config settings for account to be created. The account may already exist'

    def get_signup_page(self):
        self.browser.get_url(self.link)

    def start_process(self):
        self.get_signup_page()
        self.enter_sign_up_details()
        self.tear_down()

if __name__ == "__main__":
    CreateUserElements().start_process()