import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create an Options object to customize the behavior of Chrome
options = Options()

# Add experimental option to keep the browser open after the script ends
options.add_experimental_option("detach", True)

# Initiate the browser open one by one
Browser_List=[webdriver.Chrome(options=options),webdriver.Firefox(),webdriver.Edge()]

for driver in Browser_List:
    driver.maximize_window()
    driver.get("https://facebook.com/")

    # Identify the element locater
    driver.find_element(By.ID, "email").send_keys("Naagraaz@gmail.com")
    pass_elem = driver.find_element(By.NAME, "pass")
    pass_elem.clear()
    pass_elem.send_keys("Naagraaz@123")

    time.sleep(2)

    driver.find_element(By.NAME, "login").click()
    time.sleep(2)