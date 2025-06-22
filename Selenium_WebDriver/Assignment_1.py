########################################## Assignment ##################################################################
"""
----------
1) Open Web Browser(Chrome/Firefox/IE).
2) Open URL  https://intellipaat.com/
3) Click on Login.
4)SignUp in the website
5)Sign in after create an account
6) Capture title of the page.(Actual title)
7) Verify title of the page: "Dashboard /" (Expected)
8) close browser
"""
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://intellipaat.com/")
time.sleep(2)
driver.find_element(By.XPATH," //a[@class='login-myact']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//p[@class='woocommerce-simple-registration-login-link text-left mt-0 form-row pb-2']//a[normalize-space()='Sign Up']").click()
driver.find_element(By.NAME,"sr_firstname").send_keys("Naagraaz")
driver.find_element(By.NAME,"sr_lastname").send_keys("Kumar")
time.sleep(3)
driver.find_element(By.NAME,"email").send_keys("Naagraaz@yopmail.com")
driver.find_element(By.NAME,"password").send_keys("Kumar@1234")
driver.find_element(By.ID,"ip-vk-country-obts").click()
driver.find_element(By.XPATH,"(//select/option)[2]").click()
driver.find_element(By.NAME,"PhoneNumber_countrycode").send_keys("3216549872")
driver.find_element(By.NAME,"reg_sr_state").click()
driver.find_element(By.XPATH,"(//select/option)[6]").click()
driver.find_element(By.NAME,"register").click()






