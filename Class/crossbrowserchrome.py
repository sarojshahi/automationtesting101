#import all the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chromedriver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website
website_url = "https://www.mindrisers.com.np/"

#get the website url
driver.get(website_url)
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(3)

#get the website title
website_title = driver.title
print(f"The title of the website is {website_title}")
print("Thanks for remembering")

#calculate the height of the page
page_height = driver.execute_script("return document.body.scrollHeight")

#set the scroll speed and iteration
scroll_speed = 1000
scroll_iterations = int(page_height/scroll_speed)

#set the iteration loop
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(0.6)

#exit the stance
driver.quit()