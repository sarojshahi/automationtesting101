from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the Chromedriver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website url
website_url = "https://demoqa.com/alerts"

#get the website
driver.get(website_url)
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(3)

#locate the alert button
click_me = driver.find_element(*(By.XPATH,"//button[@id='alertButton']"))
click_me.click()
time.sleep(2)

#switch to alert
alert = driver.switch_to.alert
time.sleep(2)

#close the alert pop-up
alert.accept()
time.sleep(2)

#exit the webstance
driver.quit()

print(f"The alert button is captured and closed successfully")