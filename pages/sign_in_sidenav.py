from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
class SignIn(Page):
    SIGN_IN_SIDENAV_LNK = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    SIGN_IN_PAGE_HDR = (By.CSS_SELECTOR, "h1[class*='styles__StyledHeading-sc']")
    SIGN_IN_EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='username']")
    SIGN_IN_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[id='password']")
    SIGN_IN_PAGE_VERIFY = (By.CSS_SELECTOR, "input[id='phone']")
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")




    def click_signin_sidenav(self):
        self.wait_until_clickable(*self.SIGN_IN_SIDENAV_LNK)

    def open_signin_page(self):
        self.open('https://www.target.com/account?prehydrateClick=true')
        # calls base page directly to pass url

    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_signin_page(self):
        self.verify_text('Sign into your Target account',*self.SIGN_IN_PAGE_HDR)

    def verify_tc_opened(self):
        #self.verify_partial_url('terms-conditions/')
        self.verify_url('https://www.target.com/c/terms-conditions/-/N-4sr7l')

    def input_email(self, email):
         self.driver.find_element(*self.SIGN_IN_EMAIL_INPUT).send_keys(email)
        # this doesn't work and is not used

    def input_password(self, password):
        self.find_element(*self.SIGN_IN_EMAIL_INPUT).send_keys(password)
        # this doesn't work and is not used

