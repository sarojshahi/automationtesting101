from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set up the website
website_url = "https://demoqa.com/text-box"

#get the website url
driver.get(website_url)
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(1)

# #calculate the page height
# page_height = driver.execute_script("return document.body.scrollHeight")
#
# #Scroll Down the content
# scroll_speed  = 1000
# scroll_iterations = int(page_height/scroll_speed)
#
# #loop the performance iteration
# for _ in range(scroll_iterations):
#     driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
#     time.sleep(1)

#find the element by xpath
full_name = driver.find_element(By.XPATH, '//input[@id="userName"]')
primary_email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
current_address = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
permanent_address = driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]')
submit_button = driver.find_element(By.ID,"submit")

#fill the form
full_name.send_keys("Saroj Shahi")
primary_email.send_keys("saroj.shai.c4@gmail.com")
current_address.send_keys("Paari Butwal 02")
permanent_address.send_keys("Paari Butwal 04")
submit_button.click()
time.sleep(5)

#get the website title
website_title = driver.title
print(f" The title of the website is {website_title}")
print(f" You did it !!!")

#exit the stance
driver.quit()