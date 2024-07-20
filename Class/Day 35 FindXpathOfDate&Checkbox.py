#import all the necessary modules
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website
website_url = "https://demoqa.com/automation-practice-form"

#get the website url
driver.get(website_url)
time.sleep(1)

#maximize the window
driver.maximize_window()
time.sleep(4)

#Calculate the page height
page_height = driver.execute_script("return document.body.scrollHeight")
print(page_height)

#set the scroll speed and iteration
scroll_speed = 100
scroll_iteration = int(page_height/scroll_speed)

#loop the iteration
for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")


#close the webdriver instance
driver.quit()