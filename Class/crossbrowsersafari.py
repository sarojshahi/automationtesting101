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

#calculate the height of the webpage
page_height = driver.execute_script("return document.body.scrollHeight")

#set the scroll speed and iteration
scroll_speed = 300
scroll_iterations = int(page_height/scroll_speed)

#set the loop of page scroll
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(2)
#extract the webtitle
website_title = driver.title
print(f"the title of the website is {website_title}")

#exit the stance
driver.quit()