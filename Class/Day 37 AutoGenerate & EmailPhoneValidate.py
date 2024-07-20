#import all the necessary modules
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import re

#set up the driver as chromedrivermanager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set up the website
driver.get("https://www.mindrisers.com.np/contact-us")


#define the function for valid email pattern check using regular expression
def is_valid_email(email):
    try:
        email_pattern =  r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(email_pattern,email):
            return True
        else:
            return False

    except Exception as e:
        print(e)
        return False

#define function as valid phone checker
def is_valid_phone(phone):
    return bool(re.match(r'^\d{10}$',phone))

#maximize the window
driver.maximize_window()
time.sleep(3)


#set up the xpath of form fields
name_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
email_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
phone_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
subject_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
queries_field = driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))

#function to generate random datas
def generate_random_email():
    domain = "@test.com"
    email_length = 8
    random_string = "".join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email = random_string + domain
    return email
def generate_random_name():
    return "".join(random.choices(string.ascii_letters, k=5))

def generate_random_phonenumber():
    return "98"+"".join(random.choices(string.digits, k=8))

#using the variable to pass value into the form fields
name = generate_random_name()
email = generate_random_email()
phone = generate_random_phonenumber()
subject = ""
any_queries = "Sorry Sir, No Queries For Now"



#sending values into the form
name_field.send_keys(name)
email_field.send_keys(email)
phone_field.send_keys(phone)
subject_field.send_keys(subject)
queries_field.send_keys(any_queries)
time.sleep(4)


#if form fields are left empty, show the following
if not phone:
    print("The phone field is left empty, Please fill it ")
if not subject:
    print("The subject field is left empty, Please fill it ")
if not email:
    print("The email field should not be left empty, please fill it")
if not name:
    print("The name field should not be left empty, please fill it")
if not any_queries:
    print("The any queries field should not be left empty, please fill it")

#print if the email is valid or not

if is_valid_phone(phone):
    print("This is a valid phone")
else:
    print("This is an invalid phone")

if is_valid_email(email):
    print("This is a valid email")
else:
    print("This is an invalid email")

#close the webdriver instance
driver.quit()
print("The program to validate email and phone has been executed successfully")
