from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


class LoginPage():
    txt_username_xpath = "//input[@id='input-email']"
    txt_password_xpath = "//input[@id='input-password']"
    btn_login_xpath = "//input[@value='Login']"
    msg_myaccount_xpath = "//h2[normalize-space()='My Account']"

    def __init__(self, driver):
        self.driver = driver
    def setEmail(self, email):
        self.driver.find_element(By.XPATH,self.txt_username_xpath).send_keys(email)
    def setPassword(self, password):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def isMyAccountExist(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
        except:
            return False




