import pytest
import os
from PageObjects.Homepage import HomePage
from PageObjects.AccountRegPage import AccountRegistrationPage
import random
from utilities.readproperties import ReadConfig
from utilities.Customlogger import LogGen

  # creates instance, reads config.ini
class TestAccountRegistration:
    URL = ReadConfig.get_base_url()
    logger=LogGen.loggen()
    @pytest.mark.regression
    def test_account_registration(self, setup):
        self.logger.info("Testing AccountRegistration")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.click_my_account()
        self.hp.click_register()

        self.reg_page = AccountRegistrationPage(self.driver)

        # Generate a unique email to avoid duplication
        unique_email = f"user{random.randint(1000, 9999)}@gmail.com"

        # Use self to call all page actions
        self.reg_page.enter_first_name("John")
        self.reg_page.enter_last_name("Doe")
        self.reg_page.enter_email(unique_email)
        self.reg_page.enter_telephone("1234567890")
        self.reg_page.enter_password("Test@123")
        self.reg_page.enter_confirm_password("Test@123")
        self.reg_page.accept_privacy_policy()
        self.reg_page.click_continue()

        # Assert the success message
        msg = self.reg_page.get_confirmation_message()
        if msg == "Your Account Has Been Created!":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            self.driver.close()
            assert False
        #assert msg == "Your Account Has Been Created!", f"Expected confirmation message not found. Got: '{msg}'"
        self.logger.info("Testing AccountRegistration Complete")