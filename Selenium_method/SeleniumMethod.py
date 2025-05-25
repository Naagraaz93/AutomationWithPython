from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.durgasoft.com/registration.asp')
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Krishna")
ph_no = 1234567852
driver.find_element(By.XPATH, "//input[@id='ph_no']").send_keys(ph_no)
Email = 'Krishna@gmail.com'
driver.find_element(By.XPATH, "//input[@id='email']").send_keys(Email)
Radio = driver.find_element(By.XPATH, "(//input[@type='radio'])[1]")
print(Radio.is_displayed())
print(Radio.is_enabled())
print(Radio.is_selected())
Radio.click()
print(Radio.is_selected())
if Radio.is_selected() == True:
    print("Radio button is selected")
else:
    print("Radio button is not selected")
driver.quit()

# is_selcted(), get(), find_element(), refresh(), forward(), back(), is_displayed(), is_enabled(), is_displayed .