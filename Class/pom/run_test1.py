#import necessary modules:
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pom.pages.login_page import LoginPage

@pytest.fixture()
def driver():
    # set the chromedriver manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    #yield the driver
    yield driver
    #close the driver
    driver.quit()

@pytest.mark.parametrize("username,password",[
    ("TestQA","password"), #valid username and password
    ("invalid","password"), #invalid username and password
    ("1","1"), #invalid username and password
    ("a",""), #invalid username and password
])

def test_login(driver,username,password):
    login_page=LoginPage(driver)
    login_page.open_page("https://sagar-test-qa.vercel.app/")
    time.sleep(1)
    login_page.enter_username(username)
    time.sleep(1)
    login_page.enter_password(password)
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)

    alert_text=login_page.get_alert_text_and_accept()
    if alert_text and "Invalid username or password" in alert_text:
        print(f"Invalid username or password for {username}")
    else:
        if login_page.is_dashboard_present():
            print(f"Successful login for {username}")
        else:
            print(f"Unexpected error or login failed for {username}")