"""
✅ What is WebDriver?
----------------------
- WebDriver is a component of Selenium that allows us to interact with web browsers.
- It acts as a module in Selenium used to control browser actions like clicking buttons, entering text, etc.
- It is also an API (Application Programming Interface) that connects your test scripts with the browser.

🖥️ Examples of WebDriver Initialization:
-----------------------------------------
from selenium import webdriver

driver = webdriver.Chrome()     # For Chrome Browser
driver = webdriver.Firefox()    # For Firefox Browser
driver = webdriver.Edge()       # For Edge Browser

🧠 WebDriver Architecture
---------------------------
Selenium 3:
-----------
Selenium Language Bindings 
        ↓
JSON Wire Protocol
        ↓
Browser Drivers
        ↓
Browsers

Selenium 4:
-----------
Selenium Language Bindings 
        ↓
W3C WebDriver Protocol
        ↓
Browser Drivers
        ↓
Browsers

🔍 Note: Selenium 4 uses the W3C standard for better browser compatibility.

⚙️ Setup & Configuration of Selenium WebDriver in PyCharm
----------------------------------------------------------
✅ Pre-requisites:
- Python installed
- PyCharm installed

✅ Installation Methods:
Approach 1: Using pip
----------------------
pip install selenium

Approach 2: Using PyCharm
--------------------------
- Go to File > Settings > Project > Python Interpreter
- Click +, search for selenium, and install it.
"""
import time

################################################## Test Cases ##########################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

WebDriverWait(driver, 10).until(EC.title_is("OrangeHRM"))

act_title = driver.title
exp_title = "OrangeHRM"
if act_title.strip() == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")



