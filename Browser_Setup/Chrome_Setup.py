# Importing required modules from Selenium
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create an Options object to customize the behavior of Chrome
options = Options()

# Add experimental option to keep the browser open after the script ends
options.add_experimental_option("detach", True)

# Create a Chrome WebDriver instance with the defined options
driver = webdriver.Chrome(options=options)

# Identify the element locater
'''driver.find_element(By.ID,"email").send_keys("Naagraaz@gmail.com")
pass_elem=driver.find_element(By.NAME,"pass")
pass_elem.clear()
pass_elem.send_keys("Naagraaz@123")

time.sleep(2)

driver.find_element(By.NAME,"login").click()
time.sleep(2)
'''


driver.get("https://www.diamondchemistry.com/")
driver.maximize_window()
searchIcon = driver.find_element(By.XPATH, '//header/div[1]/div[3]/div[3]/a[1]/span[1]/span[1]/span[1]/*[1]')
searchIcon.click()
# Locate the input field for search text using XPath
enterText = driver.find_element(By.XPATH, '//*[@id="search"]')
enterText.send_keys("Ring")
enterText.send_keys(Keys.RETURN)