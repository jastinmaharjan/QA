import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_registration_form_valid_data(driver):
    driver.get("https://chulo-solutions.github.io/qa-internship/")

    # Locators for form fields and buttons
    username_field = driver.find_element(By.XPATH, "//input[@id='username']")
    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    credit_card_field = driver.find_element(By.XPATH, "//input[@id='creditCard']")
    phone_field = driver.find_element(By.XPATH, "//input[@id='telephone']")
    submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")

    # Input valid data into the form fields
    username_field.clear()
    username_field.send_keys("TestUser1")

    password_field.clear()
    password_field.send_keys("TestUser@123")

    credit_card_field.clear()
    credit_card_field.send_keys("4111111111111111")

    phone_field.clear()
    phone_field.send_keys("(977) 989-9815")

    # Submit the form
    submit_button.click()

    # Handle the alert
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Alert Text: {alert_text}")
        alert.accept()  # Dismiss the alert by clicking "OK"
    except Exception as e:
        print(f"No alert found: {e}")

    # Verify the success message
    try:
        success_message = driver.find_element(By.ID, "success").text
        assert "Registration successful!" in success_message, "Expected success message not found"
        print("Registration successful with valid data.")
    except Exception as e:
        print(f"An error occurred during validation: {e}")
        assert False, "Test failed unexpectedly"

