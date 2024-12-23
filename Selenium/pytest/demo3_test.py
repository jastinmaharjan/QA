# pytest fixtures and parametrize:
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
    driver.maximize_window()  # Maximize the browser window
    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password, expected_url, expected_message", [
    ("student", "Password123", "https://practicetestautomation.com/logged-in-successfully/", "Congratulations"),
    # Successful login
    ("incorrectUser", "Password123", None, "Your username is invalid!"),  # Invalid username
    ("student", "incorrectPassword", None, "Your password is invalid!"),  # Invalid password
])
def test_login(driver, username, password, expected_url, expected_message):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.ID, "submit")

    username_field.send_keys(username)
    password_field.send_keys(password)
    submit_button.click()

    try:
        if expected_url:
            # Positive test: Verify successful login
            assert expected_url in driver.current_url, "URL did not match expected after successful login"
            assert expected_message in driver.page_source, "Expected success message not found"
            assert driver.find_element(By.XPATH, "//a[text()='Log out']"), "Log out button not displayed"
            print(f"Login successful for username: {username}")

            # Keep the screen visible for 5 seconds
            time.sleep(5)
        else:
            # Negative test: Verify error message
            error_message = driver.find_element(By.ID, "error").text
            assert expected_message in error_message, "Expected error message not found"
            print(f"Login failed as expected for username: {username} with error: {error_message}")

            # Keep the screen visible for 5 seconds
            time.sleep(5)
    except Exception as e:
        # In case of unexpected behavior
        print(f"An error occurred: {e}")
        # Keep the screen visible for 5 seconds
        time.sleep(5)
