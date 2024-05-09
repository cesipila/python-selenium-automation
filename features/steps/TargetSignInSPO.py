from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when("Click sign in from main page")
def click_signIn_hdr(context):
    context.app.header.click_signIN_HDR()


@when("Click sign in from side navigation page")
def click_signIn_side(context):
    context.app.sign_in_sidenav.click_signin_sidenav()


@when("Input email {email_address}")
def input_email(context, email_address):
    context.driver.find_element(By.CSS_SELECTOR, "input[id='username']").send_keys(email_address)

@when("Input password {password}")
def input_password(context, password):
    context.driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)

@when("Click sign in from sign in page")
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[id='login']").click()
    sleep(3)

@then("Verify sign in form opened")
def verify_sign_in_form(context):
    context.app.sign_in_sidenav.verify_signin_page()

@then("Verify user is logged in")
def verify_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "input[id='phone']").click()
