#import the necessary module
#create browser chrome testing
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desire website
website_url= "https://www.mindrisers.com.np/"

#open the website
driver.get(website_url)
time.sleep(5)

#maximize the window size
driver.maximize_window()
time.sleep(5)

#extract the website title
website_title=driver.title
print(f"Website Title is: {website_title}")
print("code execute successfully")

#close the webdriver instance
driver.quit()





