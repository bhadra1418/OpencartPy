import pytest
from PageObjects.Homepage import HomePage
from PageObjects.Loginpage import LoginPage
from utilities.Customlogger import LogGen
from utilities.readproperties import ReadConfig

import os

class Test_LoginPage:

    URL = ReadConfig.get_base_url()
    logger = LogGen.loggen()
    user = ReadConfig.get_email()
    password = ReadConfig.get_password()
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("**** login test starting ****")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.click_my_account()
        self.hp.click_login()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage = self.lp.isMyAccountExist()
        if self.targetpage == True:
            assert True
        else:
            assert False
        self.driver.close()
        self.logger.info("**** login test completed ****")





