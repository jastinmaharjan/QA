
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desire website
website_url= "https://filebin.net/"

#open the website
driver.get(website_url)
time.sleep(2)

#maximize the window size
driver.maximize_window()
time.sleep(2)













driver.close()
