import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(3)

#set the test function
def test_google_search():
    #set the website
    website =  driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(3)
    search_button = driver.find_element(By.XPATH,"")