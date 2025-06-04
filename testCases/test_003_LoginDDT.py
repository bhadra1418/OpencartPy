
import pytest
from PageObjects.Homepage import HomePage
from PageObjects.Loginpage import LoginPage
from PageObjects.MyaccountPage import MyaccountPage
from utilities.Customlogger import LogGen
from utilities.readproperties import ReadConfig
from utilities import XLUtils

import os

class Test_LoginPage:

    URL = ReadConfig.get_base_url()
    logger = LogGen.loggen()
    path = os.path.abspath(os.curdir)+"\\testData\\Opencart_LoginData.xlsx"

    @pytest.mark.regression
    def test_loginDDT(self,setup):
        self.logger.info("**** login test starting ****")
        self.rows = XLUtils.getRowCount(self.path,"Sheet1")
        lst_status=[]
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ma = MyaccountPage(self.driver)

        for r in range(2, self.rows+1):
            self.hp.click_my_account()
            self.hp.click_login()

            self.email =XLUtils.readData(self.path,"Sheet1",r,1)
            self.password =XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()


            self.targetpage = self.lp.isMyAccountExist()
            if self.exp == "Valid":

                if self.targetpage == True:
                    self.ma.clickLogout()
                    lst_status.append('pass')
                else:
                    lst_status.append('fail')
            elif self.exp == "InValid":

                if self.targetpage == True:
                    lst_status.append('fail')
                else:
                    self.ma.clickLogout()
                    lst_status.append('pass')
        self.driver.close()
        if 'fail' not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("**** login test completed ****")





