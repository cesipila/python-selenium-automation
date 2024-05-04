class BasePage:

    def find_el(self):
        print('Finding element')

    def click(self):
        print('Clicking')

    def verify_text(self, expected_text):
        print('Checking {expected_text}')

class LoginPage(BasePage):

    def login(self, email, pw):
        print("login...")

    def verify_TC(self):
        self.verify_text('TC text')

class RegPage(BasePage):
    def register(self):
        print("register...")

login_page = LoginPage()
login_page.login()
login_page.click()