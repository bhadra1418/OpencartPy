from selenium.webdriver.common.by import By

class MyaccountPage:

    btn_logout_xpath = "//a[@class='list-group-item'][normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.btn_logout_xpath).click()