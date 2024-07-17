#import all the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

#install chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website url
website_url = "https://merolagani.com/"

#get the website url
driver.get(website_url)
time.sleep(2)

#mazimize the window
driver.maximize_window()
time.sleep(2)

#set the xpath
market = driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
market.click()
time.sleep(5)
# live_trading = driver.find_element(By.LINK_TEXT("Live Trading"))
# live_trading.click()
# time.sleep(2)


#print the success message
print("Your code is running successfully")

#close the driver instance
driver.quit()