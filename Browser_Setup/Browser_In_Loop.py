from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create an Options object to customize the behavior of Chrome
options = Options()

# Add experimental option to keep the browser open after the script ends
options.add_experimental_option("detach", True)

# Initiate the browser open one by one
Browser_List=[webdriver.Chrome(options=options),webdriver.Firefox(),webdriver.Edge()]

for driver in Browser_List:
    driver.maximize_window()
    driver.get("https://facebook.com/")