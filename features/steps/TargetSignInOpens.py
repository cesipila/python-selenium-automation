from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target site page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(3)

@when("Sign in page is opened")
def click_shopping_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.styles__LinkText-sc-1e1g60c-3").click()
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
    sleep(3)


@then("Verify Sign in form opened")
def verify_empty_card(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0").text
    print(actual_text)
    #assert 'coffee' in actual_text, f'Error! Text coffee not in {actual_text}'

