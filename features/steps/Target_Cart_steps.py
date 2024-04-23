from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# locators to get this done
search_input = (By.ID, 'search')
search_btn = (By.XPATH, '//button[@data-test="@web/Search/SearchButton"]')
cart_icon = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
header = (By.CSS_SELECTOR, "[class*='utilityHeaderWrapper]")
header_links = (By.CSS_SELECTOR, "a[id*='utilityNav']")
add_to_cart_btn = (By.CSS_SELECTOR, "[id*='utilityNav']")
side_nav_product_name = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
side_nav_add_to_cart_btn = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
cart_empty_msg = (By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0")
cart_summary_add = (By.CSS_SELECTOR, "span.styles__CartSummarySpan-sc-odscpb-3")
cart_item_title = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

@given("Open target main page")
def open_target(context):
    context.driver.get('https://www.target.com/')

@when("Search for {item}")
def Add_cart(context, item):
    context.driver.find_element(*search_input).send_keys(item)
    context.driver.find_element(*search_btn).click()
    sleep(3)

@when("Click on Cart icon")
def click_cart_icon(context):
    context.driver.find_element(*cart_icon).click()

@when("Click on Add to Cart button")
def click_add_to_cart(context):
    context.driver.find_element(*add_to_cart_btn).click()
    # # add multiple:
    # add_to_cart_button = context.driver.find_element(*add_to_cart_btn)
    # add_to_cart_button[0].click()
    # add_to_cart_button[1].click()
    # add_to_cart_button[2].click()
    # add_to_cart_button[3].click()
    # add_to_cart_button[4].click()
    # # using loops
    # for btn in add_to_cart_button[:5]:
    #     btn.click()

@when("Store product name")
def store_product_name(context):
    sleep(2)
    context.product_name = context.driver.find_element(*side_nav_product_name).text

@when("Confirm Add to Cart button from side navigation")
def confirm_add_to_cart(context):
    context.driver.find_element(*side_nav_add_to_cart_btn).click()
    sleep(2)

@when("Open cart page")
def open_cart_page(context):
    context.driver.get("https://www.target.com/cart")

@then('Verify header is shown')
def verify_header_is_shown(context):
    context.driver.find_element(*header)

@then("Verify cart has correct product")
def verify_product_name(context):
    actual_name = context.driver.find_element(*cart_item_title).text
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"

@then('Verify cart has {amount} item(s)')
def verify_amount(context, amount):
    cart_summary = context.driver.find_element(*cart_summary_add).text
    assert amount in cart_summary, f"Expected {amount} items but got {amount}"

@then("Verify your cart is empty message is shown")
def verify_cart_is_empty(context):
    actual_text = context.driver.find_element(*cart_empty_msg).text
    expected_text = 'Your cart is empty'
    assert expected_text == actual_text, f"Expected {expected_text}, but got {actual_text}"
    #context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")