#locator

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desire website
website_url= "https://www.saucedemo.com/"

#open the website
driver.get(website_url)
time.sleep(5)

#maximize the window size
driver.maximize_window()
time.sleep(5)

# locate the web element xpath
user_name=driver.find_element(*(By.XPATH,"//input[@id='user-name']"))
password=driver.find_element(*(By.XPATH,"//input[@id='password']"))
login_button=driver.find_element(*(By.XPATH,"//input[@id='login-button']"))

#fill the form
user_name.send_keys("standard_user")
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(2)
login_button.click()
time.sleep(10)

#extract the website title
website_title=driver.title
print(f"Website Title is: {website_title}")

#close the webdriver instance
driver.quit()
print("congrats locator ptah directed successfully!!!")