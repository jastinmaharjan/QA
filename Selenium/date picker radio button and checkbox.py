from tkinter.constants import FIRST

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desire website
website_url= "https://formy-project.herokuapp.com/form"

#open the website
driver.get(website_url)
time.sleep(5)

#maximize the window size
driver.maximize_window()
time.sleep(5)

#fill the form
firstName = driver.find_element(By.XPATH, value="//input[@id='first-name']")
firstName.send_keys("Justin")
time.sleep(2)

lastName = driver.find_element(By.XPATH, value="//input[@id='last-name']")
lastName.send_keys("Mhr")
time.sleep(2)

jobTitle = driver.find_element(By.XPATH, value="//input[@id='job-title']")
jobTitle.send_keys("QA")
time.sleep(2)

#scrolling
driver.execute_script("window.scrollBy(0,250);")
time.sleep(5)

#select high education level
highSchool = driver.find_element(By.XPATH, value="//input[@id='radio-button-1']")
highSchool.click()
time.sleep(2)

#select gender
male = driver.find_element(By.XPATH, value="//input[@id='checkbox-1']")
male.click()
time.sleep(5)

driver.execute_script("window.scrollBy(0,250);")

#selecting the dropdown and selecting options
selectOption =driver.find_element(By.XPATH, value="//select[@id='select-menu']")
selectOption.click()
FirstOption = driver.find_element(By.XPATH, value="//option[@value='1']")
FirstOption.click()
time.sleep(3)

#handle the calender
datepicker= driver.find_element(By.XPATH,value="//input[@id='datepicker']")
datepicker.click()
time.sleep(3)

# select the date
datetoday=driver.find_element(By.XPATH, value="//td[@class='today day']")
datetoday.click()
time.sleep(3)

# submit button
submit = driver.find_element(By.XPATH, value="//a[normalize-space()='Submit']")
submit.click()
time.sleep(3)

#close the driver instance
driver.quit()