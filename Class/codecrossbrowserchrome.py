#import the necessary module

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chromedriver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website
website_url = "https://www.mindrisers.com.np/"

#get the website
driver.get(website_url)
time.sleep(3)

#maximize the window size
driver.maximize_window()
time.sleep(3)

#extract the website title
website_title = driver.title
print(f"The Website title is {website_title}")
print("Congratulations!!! Your Automation script is working fine!!!")

#calculate the page height of the webpage
page_height = driver.execute_script("return document.body.scrollHeight")
print(page_height)

#scroll down the content
scroll_speed = 1000
scroll_iterations = int(page_height/scroll_speed)

#loop the iteration performance
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(1)

#finally quit the driver instance
driver.quit()