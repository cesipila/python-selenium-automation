from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_sidenav import SignIn


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self._main_page = MainPage(driver)
        self.header = Header(driver)
        self.sign_in_sidenav = SignIn(driver)
        self.search_results_page = SearchResultsPage(driver)
