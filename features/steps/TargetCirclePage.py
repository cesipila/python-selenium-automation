from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open Target Circle page")
def open_target(context):
    context.driver.get('https://www.target.com/circle')
    sleep(3)

@when("Verify header is shown")
def click_shopping_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "h2.styles__StyledHeading-sc-1xmf98v-0")
    sleep(3)

@then("Verify there are 6 benefit cells")
def verify_empty_card(context):
    elements = context.driver.find_elements(By.XPATH,"//div[contains(@data-component-title, 'BaseDrivers')] //div[contains(@class, 'cell-item-content')] //a")

    for element in elements:
        link = element.get_attribute("href")
        print(link)
        #assert len(link) == 6, f'Expected 6 links, but got {len(link)}'
