#import the necessary module
#scrolling the page height
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desire website
# website_url= "https://khalti.com/"
website_url= "https://www.geek-engineering.com/"

#open the website
driver.get(website_url)
time.sleep(5)

#maximize the window size
driver.maximize_window()
time.sleep(5)

#calculate the height of the page
page_height=driver.execute_script("return document.body.scrollHeight")

#scrool down
scroll_speed= 300
scroll_iteration=int(page_height/scroll_speed)

#loop to perform the scrolling increments
for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(2)

#extract the website title
website_title=driver.title
print(f"Website Title is: {website_title}")
print("code execute successfully")

#close the webdriver instance
driver.quit()