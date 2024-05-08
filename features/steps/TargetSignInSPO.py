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

@then("Verify sign in form opened")
def verify_sign_in_form(context):
    context.app.sign_in_sidenav.verify_signin_page()