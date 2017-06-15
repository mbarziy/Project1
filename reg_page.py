from base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class RegistrationPage(BasePage):
    def __init__(self, browser):
        super(RegistrationPage, self).__init__(browser)
        self.url = 'http://magento-demo.lexiconn.com/customer/account/create/'
        self.locators = {
            'first_name': '//input[@id="firstname"]',
            'last_name': '//input[@id="lastname"]',
            'email':'//input[@id="email_address"]',
            'password': '//input[@id="password"]',
            'confirmation': '//input[@id="confirmation"]',
            'newsletter_chbx': '//input[@id="is_subscribed"]',
            'register_btn': '//button[@title="Register" and @type="submit"]',
            'password_error': '//div[@id="advice-validate-cpassword-confirmation"]'
        }

    @property
    def is_password_validation_error(self):
        try:
          self.find_element('password_error')
        except NoSuchElementException:
            return False
        else:
            return True