from behave import given, when, then

@given('Open Help page for returns')
def open_target_app(context):
    context.app.help_page.open_help_returns()

# @when('Select Help topic Promotions & Coupons')
# def select_topic(context):
#     context.app.help_page.select_topic()

@when('Select Help topic {option}')
def select_topic(context, option):
    context.app.help_page.select_topic(option)

# @then('Verify Current promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_header()
#
# @then('Verify Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_header()
#
# @then('Verify Create account page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_account_header()

@then('Verify {header} page is opened')
def verify_select_option(context, header):
    context.app.help_page.verify_header(header)

