from behave import given, when, then

@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()

@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_sidenav.open_signin_page()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_app_page.get_current_window()


@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()


@when('Click on Target terms and conditions link')
def click_on_terms_and_conditions_link(context):
    context.app.sign_in_sidenav.click_tc_link()


@when('Switch to new window')
def switch_window(context):
    context.app.target_app_page.switch_to_window()

@when('Switch to the newly opened window')
def switch_new_window(context):
    context.app.sign_in_sidenav.switch_to_window()


@then('Verify Privacy Policy page opened')
def verify_pp_opened(context):
    context.app.target_app_page.verify_pp_opened()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.sign_in_sidenav.verify_tc_opened()


@then('Close current page')
def close(context):
    context.app.target_app_page.close()


@then('Return to original window')
def return_original_window(context):
    context.app.target_app_page.switch_window_by_id(context.original_window)
