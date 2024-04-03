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

# locators by ID
driver.find_element(By.ID, 'continue') # continue button
driver.find_element(By.ID, 'auth-fpp-link-bottom') # forgot password
driver.find_element(By.ID, 'ap-other-signin-issues-link') # other issues with Sign-In link
driver.find_element(By.ID, 'createAccountSubmit') # Create your Amazon account button

# locators by XPATH
driver.findelement(By.XPATH, "//input[@class='a-link-nav-icon']") # Amazon logo
driver.find_element(By.XPATH, "//input[@type='email']") # email field
driver.find_element(By.XPATH, "//input[@href= '/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']") # privacy notice
driver.find_element(By.XPATH, "//input[@class='a-expander-prompt']") # help link