#import all the neccessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#install the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website url
website_url = "https://demoqa.com/alerts"

#get the website url
driver.get(website_url)
time.sleep(2)

#maximize the window
driver.maximize_window()
time.sleep(2)

#locate the alert button
click_me = driver.find_element(*(By.XPATH,"(//button[@id='timerAlertButton'])"))
click_me.click()
time.sleep(7)

#switch to alert
alert= driver.switch_to.alert
time.sleep(2)

#close the alert
alert.accept()
time.sleep(2)

#close the instance
driver.quit()