from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the desired website
website_url = "https://meroshare.cdsc.com.np/#/login"
driver.get(website_url)
time.sleep(1)

# Maximize the window size
driver.maximize_window()
time.sleep(5)

# Select dp dropdown
selectDp = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span")))
selectDp.click()

time.sleep(2)

# Select the desired option from the dropdown
options_xpath = "//li[contains(text(), 'APPLE SECURITIES PVT. LTD. (22300)')]"
option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, options_xpath)))
option.click()

time.sleep(5)

# Close the driver
driver.quit()

print("Dropdown menu is working fine")
