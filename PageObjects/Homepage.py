from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class HomePage:
    # Locators
    my_account = "//a[@title='My Account']"
    register = "//a[normalize-space()='Register']"
    login = (By.XPATH, "//a[normalize-space()='Login']")

    def __init__(self, driver: WebDriver):
        self.driver = driver


    # Actions
    def click_my_account(self):
        self.driver.find_element(By.XPATH,self.my_account).click()

    def click_register(self):
        self.driver.find_element(By.XPATH,self.register).click()

    def click_login(self):
        self.driver.find_element(*self.login).click()