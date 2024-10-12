# using pytest fixtures
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # yield the webdriver instance
    yield driver
    #close the driver
    driver.quit()


def test_google_search(driver):
    driver.get("https://google.com")
    search_box=driver.find_element(*(By.XPATH,"//textarea[@id='APjFqb']"))
    search_box.send_keys("mindrisers.com.np")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # search and click on the link
    first_link=driver.find_element(*(By.XPATH,"//h3[contains(text(),'Best IT Training Institute in kathmandu, Nepal | M')]"))
    first_link.click()
    driver.maximize_window()
    time.sleep(5)
    print("===pytest fixtures execute successfully===")


