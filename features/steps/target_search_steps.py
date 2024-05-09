from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_HEADER = (By.XPATH, '//div[@data-test="resultsHeading"]')
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")


@given("Open Target home page")
def open_target(context):
    context.driver.get('https://www.target.com/')
    # context.app.main_page.open_main()


@when("Search for {item}")
def search_product(context, item):
    # context.driver.find_element(By.ID, 'search').send_keys(item)
    # context.driver.find_element(By.XPATH,"//button[@data-test=@web/Search/SearchButton']").click()
    # sleep(3)
    context.app.header.search_product(item)


# @then('Verify search results are shown for {item}')
# def verify_search_results(context,item):
#     actual_text = context.driver.find_element(By.XPATH, "//a[@data-test='resultsHeading']").text
#     assert 'coffee' in actual_text, f'Error! Text coffee not in {actual_text}'

@then('Verify search results are shown for {expected_item}')
def verify_expected_result(context, expected_item):
    # actual_text = context.driver.find_element(*SEARCH_RESULTS_HEADER).text
    # assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'
    context.app.search_results_page.verify_search_results(expected_item)

@then('Verify that URL has {partial_url}')
def verify_search_page_url(context, partial_url):
    context.app.search_results_page.verify_partial_url(partial_url)

@then('Verify that every product has a name and an image')
def verify_product_name(context):
    # To see All listings (comment out if you only check top ones)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    top_products = context.driver.find_elements(*LISTINGS)[:4]

    for product in top_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title != '', 'Product title not shown'
        product.find_element(*PRODUCT_IMG)
