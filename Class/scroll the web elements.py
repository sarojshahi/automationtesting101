from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#import the Chrome Driver Manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website url
website_url = "https://www.mindrisers.com.np/"

#get the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()
time.sleep(3)

#Calculate the height of the webpage
page_height = driver.execute_script("return document.body.scrollHeight")
print(page_height)

#scroll down the content
scroll_speed = 200
scroll_iterations = int(page_height/scroll_speed)

#loop the iteration performance
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed}:)")

#print the website title
website_title = driver.title
print(f"The title of the website is {website_title}")

#exit the driver stance
driver.quit()
driver