from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from sample_script import driver


class Application:

    def __init__(self, driver):
        self._main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
