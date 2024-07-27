#import all the neccesssary modules
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    #set the chrome driver manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(1)
    #yield the driver
    yield driver
    #close the driver
    driver.quit()

#set the main action path
def test_google_search(driver):
    website_url = driver.get("https://google.com")
    driver.maximize_window()
    time.sleep(2)
    search_box = driver.find_element(*(By.XPATH,"//textarea[@id='APjFqb']"))
    search_box.send_keys("mindrisers.com.np")
    search_box.submit()
    time.sleep(2)
    main_link = driver.find_element(*(By.XPATH,"//h3[contains(text(),'Best IT Training Institute in kathmandu, Nepal | M')]"))
    main_link.click()
    time.sleep(2)
    print("CONGRATS YOUR PYTEST PROGRAM IS RUNNING SUCCESFULLY")
