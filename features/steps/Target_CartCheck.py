from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when("Shopping cart is Open")
def click_shopping_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "div.styles__CartIconDiv-sc-jff2tp-1").click()
    sleep(3)

@then("Verify empty card message")
def verify_empty_card(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0").text
    print(actual_text)
    #assert 'coffee' in actual_text, f'Error! Text coffee not in {actual_text}'

