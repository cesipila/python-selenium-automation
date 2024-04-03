from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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

# click ship to menu
driver.find_element(By.ID, 'zip-code-id-btn').click()

# wait a few seconds
sleep(5)

# clear zip code field then update it
driver.find_element(By.XPATH, "//input[@value='07950']").clear()
driver.find_element(By.XPATH, "//input[@value='07950']").send_keys('07026')

# wait a few seconds
sleep(5)

# verification



# wait a few seconds
sleep(5)

driver.quit()

