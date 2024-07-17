from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

#set the Chromedriver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website url
website_url = "https://demoqa.com/automation-practice-form"

#get the website
driver.get(website_url)
time.sleep(3)

#maximize the window
driver.maximize_window()
time.sleep(3)

#wait for page load
driver.implicitly_wait(10)

#find elements of the form
first_name = driver.find_element(*(By.XPATH,"//input[@id='firstName']"))
last_name = driver.find_element(*(By.XPATH,"//input[@id='lastName']"))
email_field = driver.find_element(*(By.XPATH,"//input[@id='userEmail']"))
gender_male = driver.find_element(*(By.XPATH,"//label[normalize-space()='Male']"))
mobile_number = driver.find_element(*(By.XPATH,"//input[@id='userNumber']"))
date_of_birth = driver.find_element(*(By.XPATH,"//input[@id='dateOfBirthInput']"))

#select hobbies
hobby_sport_checkbox=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Sports']")))

#send values to the elements
first_name.send_keys("Saroj")
last_name.send_keys("Shahi")
email_field.send_keys("saroj.shai.c4@gmail.com")
gender_male.click()
mobile_number.send_keys("9818839688")
date_of_birth.clear()
date_of_birth.send_keys("15/04/1995")
#interact with the sports checkbox
driver.execute_script("arguments[0].click();", hobby_sport_checkbox)

time.sleep(2)

#close the driver stance
driver.quit()