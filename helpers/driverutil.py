__author__ = 'Southekal'

from selenium import webdriver
import ConfigParser

"""config settings"""
config = ConfigParser.RawConfigParser()
config.read('./default.cfg')


class WebDriver(object):
    """
        Initializing WebDriver Elements
    """

    def __init__(self):
        self.driver = None

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def setUp_mobile(self):
        mobile_width = config.get('ScreenSize', 'mobile_width')
        mobile_height = config.get('ScreenSize', 'mobile_height')

        self.driver = webdriver.Firefox()
        self.driver.set_window_size(mobile_width, mobile_height)

    def get_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_id(self, id_val):
        return self.driver.find_elements_by_id(id_val)

    def get_class(self, class_val):
        return self.driver.find_elements_by_class_name(class_val)

    def get_css(self, css_val):
        return self.driver.find_elements_by_css_selector(css_val)

    def get_name(self, name):
        return self.driver.find_elements_by_name(name)

    def get_current_url(self):
        return self.driver.current_url

    def tearDown(self):
        self.driver.close()
        self.driver.quit()



