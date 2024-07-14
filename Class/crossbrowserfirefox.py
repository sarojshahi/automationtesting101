from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

#set up Gecko driver
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#set up website url
website_url = "https://www.mindrisers.com.np/"

#open the website url
driver.get(website_url)
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(3)

#extract the website url
website_title = driver.title
print(f"The title of the website is {website_title}")
print("Yeahh boy")


#calculate the height of the page
page_height = driver.execute_script("return document.body.scrollHeight")
print(page_height)

#set the scroll speed and iterations
scroll_speed = 100
scroll_iterations = int(page_height/scroll_speed)

#set the loop for page scroll
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(1)

#exit the firefox stance
driver.quit()