from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

#set the chromedrivermanager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website
website_url = "https://www.sharesansar.com/#"

#get the website
driver.get(website_url)
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(5)

#Redirect to the market overview tab
market = driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
market.click()
time.sleep(4)

#selecting from the dropdown
market_overview = driver.find_element(By.LINK_TEXT, "Market Overview")
market_overview.click()
time.sleep(5)

#locating the search bar
search_bar = driver.find_element(*(By.XPATH,"//input[@id='company_search']"))
search_bar.send_keys("JBLB")
time.sleep(2)
search_bar.submit()
time.sleep(3)

#hit the news link
news = driver.find_element(*(By.XPATH,"//a[@id='btn_cnews']"))
news.click()
time.sleep(3)

#scroll to the bottom
target_y=2000
scroll_distance = 1000
current_y = 0
#loop the scroll distance
while current_y<target_y:
    driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
    current_y += scroll_distance
    time.sleep(4)

#hit the pagination
next_button = driver.find_element(*(By.XPATH,"//a[@id='myTableCNews_next']"))
next_button.click()
time.sleep(4)



print("your task is successful")

#close the website
driver.quit()
