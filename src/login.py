__author__ = 'Southekal'

from helpers import driverutil
from helpers import locators
import time
import requests
import ConfigParser

"""config settings"""
config = ConfigParser.RawConfigParser()
config.read('./default.cfg')


class TestPageElements(object):

    def __init__(self):
        """
        initializing objects needed by modules
        """
        self.login_page = locators.LoginPageLocators()
        self.link = self.login_page.LOGIN_URL
        self.job_seeker_id = self.login_page.JOB_SEEKER_ID
        self.email_name = self.login_page.EMAIL_NAME
        self.password_name = self.login_page.PASSWORD_NAME
        self.sign_in = self.login_page.SIGN_IN_NAME
        self.successful_login_link = self.login_page.SUCCESS_LOGIN_URL
        self.invalid_email_error = self.login_page.EMAIL_ERROR_CSS
        self.invalid_password_error = self.login_page.PASSWORD_ERROR_CSS
        self.missing_password_error = self.login_page.PASSWORD_MISSING_CSS
        self.email = config.get('Login', 'email')
        self.password = config.get('Login', 'password')
        self.failed_email = config.get('FailedEmailLogin', 'email')
        self.failed_password = config.get('FailedPasswordLogin', 'password')

    def tear_down(self, browser):
        """
        closing process and browser
        """
        print '[INFO]: Shutting down the browser'
        browser.tearDown()

    def successful_logged_in_page_status(self, browser):
        """
        checking for page status 200OK on successful login
        """
        print '[INFO]: Checking the post successful login page HTTP status'
        r = requests.get(browser.get_current_url())
        print '[INFO]: HTTP status is {0}'.format(r.status_code)
        assert r.status_code == 200

    def successful_logged_in(self, browser):
        """
        assert after login the user is redirected to the correct logged in page
        """
        print '[INFO]: Successful post login url: {0}'.format(browser.get_current_url())
        assert browser.get_current_url() == self.successful_login_link

    def successful_login_details(self, browser):
        """
        logs in a user with valid email address and password
        """
        email_elem = browser.get_name(self.email_name)
        print '[INFO]: Entering valid email id'
        time.sleep(3)  # delays for 3 seconds
        email_elem[0].clear()
        email_elem[0].send_keys(self.email)

        time.sleep(3)  # delays for 3 seconds
        password_elem = browser.get_name(self.password_name)
        print '[INFO]: Entering valid password'
        password_elem[0].clear()
        password_elem[0].send_keys(self.password)

        print '[INFO]: Clicking on Submit button'
        time.sleep(3)  # delays for 3 seconds
        browser.get_name(self.sign_in)[0].click()

    def missing_password_login_details(self, browser):
        """
        attempts to log in a user with valid email address and empty password field
        """
        email_elem = browser.get_name(self.email_name)
        print '[INFO]: Entering a valid email address while leaving password empty'
        time.sleep(3)  # delays for 3 seconds
        email_elem[0].clear()
        email_elem[0].send_keys(self.email)

        time.sleep(3)
        password_elem = browser.get_name(self.password_name)
        password_elem[0].clear()
        time.sleep(3)

        browser.get_name(self.sign_in)[0].click()
        print '[INFO]: Checking for {This field is required.} flash message'
        time.sleep(3)
        assert len(browser.get_css(self.missing_password_error)) > 0

    def missing_email_login_details(self, browser):
        """
        attempts to log in a user with empty email address field and entered password
        """
        email_elem = browser.get_name(self.email_name)
        time.sleep(3)  # delays for 3 seconds
        email_elem[0].clear()

        print '[INFO]: Entering the password while leaving email empty'
        password_elem = browser.get_name(self.password_name)
        password_elem[0].clear()
        password_elem[0].send_keys(self.password)

        browser.get_name(self.sign_in)[0].click()
        print '[INFO]: Checking for {Please enter a valid email address} flash message'
        time.sleep(3)
        assert len(browser.get_css(self.invalid_email_error)) > 0

    def failed_password_login_details(self, browser):
        """
        attempts to log in a user with valid email address field and invalid password
        """
        email_elem = browser.get_name(self.email_name)
        time.sleep(3)  # delays for 3 seconds
        email_elem[0].clear()
        email_elem[0].send_keys(self.email)

        print '[INFO]: Entering an invalid password'
        password_elem = browser.get_name(self.password_name)
        password_elem[0].clear()
        password_elem[0].send_keys(self.failed_password)

        browser.get_name(self.sign_in)[0].click()
        print '[INFO]: Checking for {Incorrect email or password. Please try again.} flash message'
        time.sleep(3)
        assert len(browser.get_css(self.invalid_password_error)) > 0

    def failed_email_login_details(self, browser):
        """
        attempts to log in a user with invalid email address field and valid password
        """
        email_elem = browser.get_name(self.email_name)
        print '[INFO]: Entering an invalid email id'
        time.sleep(3)  # delays for 3 seconds
        email_elem[0].clear()
        email_elem[0].send_keys(self.failed_email)

        password_elem = browser.get_name(self.password_name)
        password_elem[0].clear()
        password_elem[0].send_keys(self.password)

        browser.get_name(self.sign_in)[0].click()
        print '[INFO]: Checking for {Please enter a valid email address} flash message'
        time.sleep(3)
        assert len(browser.get_css(self.invalid_email_error)) > 0

    def missing_email_password_details(self, browser):
        """
        attempts to log in a user with empty email address field and empty password field
        """
        email_elem = browser.get_name(self.email_name)
        print '[INFO]: Leaving email id empty'
        time.sleep(3)  # delays for 3 seconds
        email_elem[0].clear()

        print '[INFO]: Leaving password empty'
        password_elem = browser.get_name(self.password_name)
        password_elem[0].clear()

        browser.get_name(self.sign_in)[0].click()
        print '[INFO]: Checking for {Please enter a valid email address} flash message'
        print '[INFO]: Checking for {This field is required.} flash message'
        time.sleep(3)
        assert len(browser.get_css(self.invalid_email_error)) > 0
        assert len(browser.get_css(self.missing_password_error)) > 0

    def login_page_elements(self, browser):
        """
        checks for the presence of email field, password field and a submit button
        """
        print '[INFO]: Checking for presence of the Email Address section'
        assert len(browser.get_name(self.email_name)) > 0

        print '[INFO]: Checking for presence of the Password section'
        assert len(browser.get_name(self.password_name)) > 0

        print '[INFO]: Checking for presence of the Submit Button'
        assert len(browser.get_name(self.sign_in)) > 0

    def switch_to_job_seeker_view(self, browser):
        """
        switches view to the JOB SEEKER tab
        """
        print '[INFO]: Checking for presence of Job Seeker View Tab'
        assert len(browser.get_id(self.job_seeker_id)) > 0
        print '[INFO]: Switching to Job Seeker View for Login'
        browser.get_id(self.job_seeker_id)[0].click()

    def login_page_title(self, browser):
        """
        checks for login page title
        """
        title_holder = []
        print '[INFO]: Checking for page title for LOGIN'
        title_holder.append(browser.get_title())
        assert len(title_holder) > 0

    def login_page_status(self):
        """
        checks for 200OK page status on accessing the login page
        """
        print '[INFO]: Checking the login page HTTP status'
        r = requests.get(self.link)
        print '[INFO]: HTTP status is {0}'.format(r.status_code)
        assert r.status_code == 200

    def get_login_page(self, browser):
        """
        opens a Firefox session of the login page
        """
        print '[INFO]: Getting the login page'
        browser.get_url(self.link)
        print '[INFO]: Login page url accessed: {0}'.format(browser.get_current_url())
        assert browser.get_current_url() == self.link

    def start_up(self, browser):
        """
        initializes the firefox webdriver
        """
        print '[INFO]: Initializing Firefox Selenium WebDriver'
        browser.setUp()

    def test_start_process(self):
        """
        main function to run the tests
        """
        print '[INFO]: Starting LoginPage Test'
        browser = driverutil.WebDriver()
        yield self.start_up, browser
        yield self.get_login_page, browser
        yield self.login_page_status
        yield self.login_page_title, browser
        yield self.switch_to_job_seeker_view, browser
        yield self.login_page_elements, browser
        yield self.missing_email_password_details, browser
        yield self.failed_email_login_details, browser
        yield self.failed_password_login_details, browser
        yield self.missing_email_login_details, browser
        yield self.missing_password_login_details, browser
        yield self.successful_login_details, browser
        yield self.successful_logged_in, browser
        yield self.successful_logged_in_page_status, browser
        yield self.tear_down, browser
