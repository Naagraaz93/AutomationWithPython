from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create an Options object to customize the behavior of Chrome
options = Options()

# Add experimental option to keep the browser open after the script ends
options.add_experimental_option("detach", True)


browser = 'firefox'  # or 'chrome', 'firefox', 'edge'

# Initiate the browser
if browser.lower() == 'chrome':
    driver = webdriver.Chrome(options=options)
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()
elif browser.lower() == 'edge':
    driver = webdriver.Edge()

driver.maximize_window()
driver.get("https://facebook.com/")