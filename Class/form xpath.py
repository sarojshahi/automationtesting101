from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#install the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website url
website_url = "https://www.mindrisers.com.np/contact-us"

#get the website
driver.get(website_url)
time.sleep(2)

#Maximize the window
driver.maximize_window()
time.sleep(2)

#locate the webfrom
full_name = driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
email_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
phone = driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
subject = driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
any_queries = driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))
# submit = driver.find_element(*(By.XPATH,"//button[normalize-space()='Submit']"))

#input the data
full_name.send_keys("Saroj Shahi")
email_field.send_keys("saroj.shai.c4@gmail.com")
phone.send_keys("9818839688")
subject.send_keys("testing")
any_queries.send_keys("this is a selenium testing 101")
# submit.click()
time.sleep(5)

#close the instance
driver.quit()