
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com/')
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Naagraaz")
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("Krrish")
driver.find_element(By.XPATH,"//select[@id='day']/option[10]").click()
driver.find_element(By.XPATH,"//select[@id='month']/option[7]").click()
driver.find_element(By.XPATH,"//select[@id='year']/option[33]").click()
driver.find_element(By.XPATH,"(//input[@type='radio'])[1]").click()
driver.find_element(By.XPATH,"(//input[@name='reg_email__'])").send_keys("Naagraaz@gmail.com")
driver.find_element(By.XPATH,"(//input[@type='password'])").send_keys("Naagraaz@1234")
driver.find_element(By.XPATH,"(//button[@type='submit'])[1]").click()

