import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#set up driver as Chrome Driver Manager
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    yield driver
    driver.quit()

@pytest.mark.parametrize("username,password",[
    ("TestQA","password"),
    ("ABC","CDF"),
    ("TestQA","12345"),
    ("Saroj","password"),
    ("TestQA","password"),
    ("Hello","World")
])

def test_login(driver, username, password):
    driver.get("https://sagar-test-qa.vercel.app/")
    driver.maximize_window()
    username_field = driver.find_element(By.XPATH,"//input[@id='username']")
    password_field = driver.find_element(By.XPATH,"//input[@id='password']")
    login_button = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

        #check if the username or password is incorrect
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        assert "Invalid username or password" in alert_text
        print(f"Invalid username or password for {username}")

        #check if the username and password is correct
    except:
        time.sleep(2)
        page_source = driver.page_source
        if "Welcome to the Dashboard" in page_source:
            print(f"Valid Username or Password for user: {username}")
        else:
            print("Unexpected Error!! Please try again later!")