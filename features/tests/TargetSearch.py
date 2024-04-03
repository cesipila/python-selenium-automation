from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

### steps
# click search input box
driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").click()

# enter search item/category
driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").send_keys('Coffee')

# click the search button
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(5)

# check results page and counts appeared for the search query
actual_text = driver.find_element(By.XPATH, "//span[@class='h-margin-r-x1']").text
print(actual_text)

sleep(5)