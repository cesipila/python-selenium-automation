from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep
class Header(Page):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGN_IN_HDR_LNK = (By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")

    def search_product(self, item):
        self.input_text({item}, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.wait_until_clickable(*self.CART_ICON)
        self.save_screenshot('cart.png')

    def click_signIN_HDR(self):
        self.wait_until_clickable(*self.SIGN_IN_HDR_LNK)