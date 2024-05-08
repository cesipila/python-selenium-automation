from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
class SignIn(Page):
    SIGN_IN_SIDENAV_LNK = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    SIGN_IN_PAGE_HDR = (By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc']")


    def click_signin_sidenav(self):
        self.wait_until_clickable(*self.SIGN_IN_SIDENAV_LNK)

    def verify_signin_page(self):
        self.verify_text('Sign into your Target account',*self.SIGN_IN_PAGE_HDR)
