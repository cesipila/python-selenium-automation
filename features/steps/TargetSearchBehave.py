from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target home page")
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when("Search for product")
def click_shopping_cart(context):
    context.driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").click()
    context.driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").send_keys('Coffee')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(3)

# @then("Verify search results are shown")
# def verify_empty_card(context):
#     actual_text = context.driver.find_element(By.XPATH, "//span[@class='h-margin-r-x1']").text
#     print(actual_text)
#     #assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'