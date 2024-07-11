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

#exit the firefox stance
driver.quit()