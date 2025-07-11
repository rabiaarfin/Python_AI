from Pages.BasePage import  BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
class LoginPage(BasePage):
    """By locators-OR"""
    Email=(By.ID, "username")
    Password=(By.ID,"password")
    LoginButton=(By.ID,"loginBtn")
    SIGNUP_link=(By.CLASS_NAME,"TruncateString__ReversedTruncateStringTail-jbtxd0-1")
    """ Constructor of Page class"""

    def __init__(self,driver):
        super().__init__(driver)
        driver.get(TestData.BASE_URL)

    """Page Actions"""
    """this is used to get page title"""

    def get_login_Page_title(self):
        return self.get_title(TestData.loginPageTitle)

    """This is used to check sign up link"""
    def is_signup_link_exist(self):

        return self.is_visible(self.SIGNUP_link)
    """This is used to click on login"""
    def do_login(self,username,password):
        self.do_send_keys(self.Email,username)
        self.do_send_keys(self.Password,password)
        self.do_click(self.LoginButton)
        return "You are login"



