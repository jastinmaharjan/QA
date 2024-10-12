#pytest fixtures and parametrize:
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password", [
    ("TestQA", "password"),  # Valid username and password
    ("invaliduser", "invalidpass"),  # invalid username and password
    ("1", "a"),                      # invalid username and password (invalid)
    ("user3", "pass3"),              # inValid username and password
])
def test_login(driver, username, password):
    driver.get("https://sagar-test-qa.vercel.app/")
    username_field = driver.find_element(By.XPATH, "//input[@id='username']")
    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    try:
        # Check if an alert is present
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert "Invalid username or password" in alert_text
        print(f"Invalid username or password for {username}")
    except:
        # No alert means login was successful
        time.sleep(2)
        page_source = driver.page_source
        if "Welcome to the Dashboard" in page_source:
            print(f"Login successful for {username}")
        else:
            print(f"Unexpected error or login failed for {username}")
