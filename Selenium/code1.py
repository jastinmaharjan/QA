#import the necessary module
#create browser chrome testing

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome driver manager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open the desire website








