from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desire website
website_url= "https://demoqa.com/alerts"

#open the website
driver.get(website_url)
time.sleep(3)

#maximize the window size
driver.maximize_window()
time.sleep(3)

#locate and click the alert button
click_me=driver.find_element(*(By.XPATH,"//button[@id='alertButton']"))
click_me.click()
time.sleep(4)

#close the driver instance
driver.quit()
