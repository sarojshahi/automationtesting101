from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the Chromedriver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website url
website_url = "https://www.sharesansar.com/"

#get the website
driver.get(website_url)
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(3)

#find the element by the xpath and link text
market = driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
market.click()
time.sleep(4)
overview = driver.find_element(By.LINK_TEXT,"Market Overview")
overview.click()
time.sleep(5)

#exit the webstance
driver.quit()

print(f"The linked button is captured and closed successfully")