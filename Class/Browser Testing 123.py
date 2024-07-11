from selenium import webdriver
from selenium.webdriver.chrome.service import service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the Chromedriver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website url
website_url = "https://www.mindrisers.com.np/"

#get the website
driver.get(website_url)
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(3)

#EXTRACT THE WEBSITE TITLE
website_title = driver.title
print(f"The title of the website is {website_title}")
print(" Your task is well done ")

#exit the driver instance
driver.quit()
