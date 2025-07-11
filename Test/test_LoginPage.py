import pytest
from Test.test_base import BaseTest
from Pages.Login import LoginPage
from Config.config import TestData
class Test_login(BaseTest):
    def test_signup_link_visible(self):
        self.LoginPage=LoginPage(self.driver)
        flag=self.LoginPage.is_signup_link_exist()
        assert  flag

    def test_login_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        title = self.LoginPage.get_login_Page_title()
        assert title == TestData.loginPageTitle




    def test_login(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        self.LoginPage.do_click(LoginPage.LoginButton)




