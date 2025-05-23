import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
driver.get('https://www.durgasoft.com/registration.asp')
driver.maximize_window()

# Locators
'''
8 types of locator:
id --> find_element(By.ID,"value")
class name -->
name --> find_element(By.NAME,"value")
xpath --> find_element(By.XPATH,"//input[@id='name']")
tagname --> find_element(By.TAGNAME,"a")
link text
partial link text
css selector

'''
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Krishna")
ph_no=1234567852
driver.find_element(By.XPATH,"//input[@id='ph_no']").send_keys(ph_no)
Email='Krishna@gmail.com'
driver.find_element(By.XPATH,"//input[@id='email']").send_keys(Email)
driver.find_element(By.XPATH,"(//input[@type='radio'])[1]").click()
driver.find_element(By.XPATH,"(//input[@type='checkbox'])[12]").click()
driver.find_element(By.XPATH,"(//input[@type='text'])[4]").send_keys("12-10-2025")
driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys("3:00 PM")
driver.find_element(By.XPATH,"//textarea[@id='desc']").send_keys("I am a fresher")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

driver.quit()

