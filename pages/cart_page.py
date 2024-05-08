from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "div[data-test='boxEmptyMsg']")
    Add_To_Cart_Btn = (By.CSS_SELECTOR, "button[type='button'][id*='addToCartButtonOrTextIdFor'][data-test='chooseOptionsButton']")

    def verify_cart_empty_message(self):
        self.verify_text('Your cart is empty',*self.CART_EMPTY_MSG)
    def add_single_product(self):
        self.find_element(*self.Add_To_Cart_Btn).click()

    def add_multiple_product(self):
        Add_To_Cart = self.find_elements(*self.Add_To_Cart_Btn)
        Add_To_Cart[0].click()
        Add_To_Cart[1].click()
        Add_To_Cart[2].click()
        Add_To_Cart[3].click()
        Add_To_Cart[4].click()

        # # using loops
        # for btn in add_to_cart_button[:5]:
        #     btn.click()

