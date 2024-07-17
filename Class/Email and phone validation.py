#import all the necessary modules
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#install the Chrome Driver Mangaer
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#define the function as email validation
def is_valid_email(email):
    try:
        #check the format using regular expression(re)
        email_pattern = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

        if re.search(email_pattern, email):
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False

def is_valid_phone(phone):
    return bool(re.match(r'^\d{10}$',phone))

#setting up the web url
driver.get("https://www.mindrisers.com.np/contact-us")

#maximize the window
driver.maximize_window()
time.sleep(2)

#setting up the window scroll
target_y = 6000
scroll_distance = 1000
current_y = 0

#loop the scroll iteration
while current_y<target_y:
    driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
    current_y += scroll_distance
    time.sleep(3)

#interact with the path locator
name_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
email_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
phone_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
subject_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
any_queries_field = driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))

full_name = "Saroj Shahi"
email = "saroj@@gmail..com"
phone =  "981883968"
subject = "QA"
any_queries = "NO Nothing"



if is_valid_email(email):
    print("The email is valid ")
else:
    print("The email is invalid")

if is_valid_phone(phone):
    print("The given Phone number is valid")
else:
    print("The given Phone number is invalid")

#clearing and giving the values in the field
name_field.clear()
name_field.send_keys(full_name)
email_field.clear()
email_field.send_keys(email)
phone_field.clear()
phone_field.send_keys(phone)
subject_field.clear()
subject_field.send_keys(subject)
any_queries_field.clear()
any_queries_field.send_keys(any_queries)
time.sleep(4)


driver.quit()
print("The email and phone validation is successfully executed")