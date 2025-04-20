from selenium import webdriver

driver = webdriver.Firefox()  # Capital 'E'
driver.get('https://selenium.dev/')
driver.quit()
