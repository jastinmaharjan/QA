from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desire website
website_url= "https://merolagani.com/"

#open the website
driver.get(website_url)
time.sleep(1)

#maximize the window size
driver.maximize_window()
time.sleep(1)

market= driver.find_element(By.XPATH,value="//a[normalize-space()='Market']")
market.click()
time.sleep(2)

indices= driver.find_element(By.LINK_TEXT, value="Indices")
indices.click()
time.sleep(2)




#close the driver
driver.quit()

print("Dropdown menu is working fine")