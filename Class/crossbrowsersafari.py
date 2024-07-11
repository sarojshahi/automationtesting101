from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new Safari session
driver = webdriver.Safari()

#set the website
website_url = "https://khalti.com"

#get the website
driver.get(website_url)
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(3)

#extract the webtitle
website_title = driver.title
print(f"the title of the website is {website_title}")

#exit the stance
driver.quit()