from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
driver.maximize_window()
driver.get("https://selenium.dev/")
