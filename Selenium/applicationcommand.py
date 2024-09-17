from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desire website
website_url= "https://www.mindrisers.com.np/contact-us"

#open the website
driver.get(website_url)
time.sleep(5)

#maximize the window size
driver.maximize_window()
time.sleep(5)

#locate the webelement by using locator
Name= driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
Email= driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
Phone= driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
Subject= driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
AnyQueries= driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))

#fill the form
Name.send_keys("test")
time.sleep(3)
Email.send_keys("test@gmail.com")
time.sleep(3)
Phone.send_keys("98612345678")
Subject.send_keys("QA")
time.sleep(3)
AnyQueries.send_keys("Hello Mindrisers")

#use of application command
#1 extract and print website title
website_title=driver.title
print(f"website title is ", {website_title})

#2. get the curernt url
current_url= driver.current_url
print(f"Current url is: ", {current_url})

#close the webdriver instance
driver.quit()

print("congrats!")