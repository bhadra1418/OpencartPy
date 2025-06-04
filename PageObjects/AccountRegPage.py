from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AccountRegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Locators
    firstname_name = (By.NAME, "firstname")
    lastname_name = (By.NAME, "lastname")
    email_name = (By.NAME, "email")
    telephone_name = (By.NAME, "telephone")
    password_name = (By.NAME, "password")
    confirm_password_name = (By.NAME, "confirm")
    privacy_policy_name = (By.NAME, "agree")
    continue_button_xpath = (By.XPATH, "//input[@value='Continue']")
    confirm_msg_xpath = (By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")

    # Actions
    def enter_first_name(self, value):
        self.driver.find_element(*self.firstname_name).send_keys(value)

    def enter_last_name(self, value):
        self.driver.find_element(*self.lastname_name).send_keys(value)

    def enter_email(self, value):
        self.driver.find_element(*self.email_name).send_keys(value)

    def enter_telephone(self, value):
        self.driver.find_element(*self.telephone_name).send_keys(value)

    def enter_password(self, value):
        self.driver.find_element(*self.password_name).send_keys(value)

    def enter_confirm_password(self, value):
        self.driver.find_element(*self.confirm_password_name).send_keys(value)

    def accept_privacy_policy(self):
        self.driver.find_element(*self.privacy_policy_name).click()

    def click_continue(self):
        self.driver.find_element(*self.continue_button_xpath).click()

    def get_confirmation_message(self):
        try:
            return self.driver.find_element(*self.confirm_msg_xpath).text
        except:
            None