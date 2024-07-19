import random
import string

from selenium import webdriver
import re
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#define the function as email validation
def is_valid_email(email):
    try:
        #check the format using Regular Expression(re)
        email_pattern = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(email_pattern,email):
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False

#define the function as phone validation
def is_valid_phone(phone):
    return bool(re.match(r'^\d{10}$',phone))

#open the website url
driver.get("https://www.mindrisers.com.np/contact-us")

driver.maximize_window()

# #set the scroll parameter
# target_y=6000
# scroll_distance = 500
# current_y=0
#
# #set the loop scoll iteration
# while current_y<target_y:
#     driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
#     current_y += scroll_distance
#     time.sleep(2)

#interact with the path locator
name_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
email_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
phone_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
subject_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
queries_field = driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))


#function to generate random email:
def generate_random_email():
    domain = "test.com"
    email_length = 8
    random_string = ''.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email = random_string + "@" + domain
    return email

def generate_random_name():
    return "".join(random.choices(string.ascii_letters, k = 5))

def generate_random_phone():
    phone = "98"+''.join(random.choices(string.digits,k=8))
    return phone

#passing the value in the variable
name= generate_random_name()
email = generate_random_email()
phone = generate_random_phone()
subject="Quality Assurance"
any_queries="Yes Please"

time.sleep(2)

#check the validity of the email
if is_valid_email(email):
    print("The given email is valid")
else:
    print("The given email is invalid")

#check the phone and email are empty or not
if not email:
    print("The Email field is empty")

if not phone:
    print("The Phone field is empty")


#Sending values to the forms
name_field.send_keys(name)
email_field.send_keys(email)
phone_field.send_keys(phone)
subject_field.send_keys(subject)
queries_field.send_keys(any_queries)

time.sleep(2)

#check the validity of the phone
if is_valid_phone(phone):
    print("The given number is valid")
else:
    print("the given number is invalid")


#close the web driver instance
driver.quit()
print("Email Validation is executed successfully")