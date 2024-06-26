from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, '//div[@data-test="resultsHeading"]')

    def verify_search_results(self, expected_item):
        actual_text = self.find_element(*self.SEARCH_RESULTS_HEADER).text
        assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'
        # print(expected_item, actual_text)
        # print('Expected item:', expected_item, ' Actual item:', actual_text)
