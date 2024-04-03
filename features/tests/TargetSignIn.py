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

# click sign-in button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()

# wait 5 secs
sleep(5)


# click sign-in from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

# wait 5 secs
sleep(5)

### Verifications
# Check for page title
actual_text = driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text
sample_text = 'Sign into your Target account'
if actual_text != sample_text:
    print(f'Invalid text used on the page')
elif actual_text == sample_text:
    print(f'Valid text used on the page')

# Check for sign in button text
Sign_in_button = driver.find_element(By.ID, 'login').text
sign_in_button_sample = 'Sign in with password'
if sign_in_button_sample != Sign_in_button:
    print(f'Invalid text for sign in button')
elif sign_in_button_sample == Sign_in_button:
    print(f'Valid text for sign in button')
