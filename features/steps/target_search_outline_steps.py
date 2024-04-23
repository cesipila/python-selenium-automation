from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given('Open Target page')
# def open_target(context):
#     context.driver.get('https://www.target.com/')

# @when("Search for {item}")
# def search_product(context, item):
#     context.driver.find_element(By.ID, 'search').send_keys(item)
#     context.driver.find_element(By.XPATH,"//button[@data-test=@web/Search/SearchButton']").click()
#     sleep(3)

@then('Verify search results for {expected_item}')
def verify_search_results(context, expected_item):
    actual_text = context.driver.find_element(By.XPATH, "//a[@data-test='resultsHeading']").text
    assert expected_item in actual_text, f'Error! Text coffee not in {actual_text}'
