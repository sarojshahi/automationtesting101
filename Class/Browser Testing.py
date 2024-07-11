from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chromedrivermanager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website
website_url = "https://www.mindrisers.com.np/"

#get the website
driver.get(website_url)
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(5)

#extract the website title
website_title = driver.title
print(f"The title of the website is {website_title}")
print("your task is successful")

#close the website
driver.quit()
