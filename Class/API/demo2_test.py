#import all the necessary modules
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#function test_google_search
def test_google_search():
    #set the chrome driver manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(1)

    #set the actual action path
    website_url = driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(2)
    search_button = driver.find_element(*(By.XPATH,"//textarea[@id='APjFqb']"))
    search_button.send_keys("mindrisers.com.np")
    search_button.submit()
    time.sleep(2)
    #main link
    main_link = driver.find_element(*(By.XPATH,"//h3[contains(text(),'Best IT Training Institute in kathmandu, Nepal | M')]"))
    main_link.click()
    time.sleep(2)
    print("YOUR FIRST PYTEST PROGRAM IS SUCCESSFULL")
    driver.quit()
