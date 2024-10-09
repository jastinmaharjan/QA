from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desired website
website_url= "https://filebin.net/"
driver.get(website_url)
time.sleep(2)

#maximize the window size
driver.maximize_window()
time.sleep(2)

# Select the file input element and upload a file
select_files_to_upload = driver.find_element(By.XPATH, "//input[@id='fileField']")
select_files_to_upload.send_keys("C:/Users/LENOVO/OneDrive/Desktop/lion.jpeg")
time.sleep(2)

# For download, click on the dropdown menu
download = driver.find_element(By.XPATH, "//a[@id='dropdownFileMenuButton']")
download.click()
time.sleep(3)

# Click on the 'Download file' link
download_file = driver.find_element(By.XPATH, "//a[normalize-space()='Download file']")
download_file.click()
time.sleep(3)

driver.find_element(By.XPATH,"/html/body/div[3]/p/a[2]").click()
time.sleep(5)
# Close the browser window
driver.close()
