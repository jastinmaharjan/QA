from selenium import webdriver
from selenium.webdriver.common.by import By


# Set the path to the ChromeDriver executable
chrome_driver_path = "path/to/chromedriver"
# Navigate to a web page
driver.get("https://example.com")


# 1. ID Locator:
# Syntax: driver.find_element(By.ID, "element_id")
driver.find_element(By.ID, "element_id").send_keys("example_input")


# 2. Name Locator:
# Syntax: driver.find_element(By.NAME, "element_name")
driver.find_element(By.NAME, "element_name").send_keys("example_input")


# 3. XPath Locator:
# Syntax: driver.find_element(By.XPATH, "xpath_expression")
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("example_input")


# 4. CSS Selector Locator:
# Syntax: driver.find_element(By.CSS_SELECTOR, "css_selector")
driver.find_element(By.CSS_SELECTOR, "input#username").send_keys("example_input")


# 5. Link Text Locator:
# Syntax: driver.find_element(By.LINK_TEXT, "link_text")
driver.find_element(By.LINK_TEXT, "Click here for more information").click()


# 6. Partial Link Text Locator:
# Syntax: driver.find_element(By.PARTIAL_LINK_TEXT, "partial_link_text")
driver.find_element(By.PARTIAL_LINK_TEXT, "more information").click()


# 7. Tag Name Locator:
# Syntax: driver.find_element(By.TAG_NAME, "tag_name")
driver.find_element(By.TAG_NAME, "a").click()


# 8. Class Name Locator:
# Syntax: driver.find_element(By.CLASS_NAME, "class_name")
driver.find_element(By.CLASS_NAME, "login-button").click()


# Close the browser when done
driver.quit()





