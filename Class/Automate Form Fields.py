from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import re
import string
import random

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#set the website
driver.get("https://www.mindrisers.com.np/contact-us")

#maximize the window
driver.maximize_window()
time.sleep(2)

#define a function to validate email
def is_valid_email(email):
    try:
        email_pattern = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(email_pattern, email):
            return True
        else:
            return False

    except Exception as e:
        return False

def is_valid_phone(phone):
    return bool(re.match(r'^\d{10}$',phone))

#generate the random email
def generate_random_email():
    domain = "@test.com"
    email_length = 8
    random_email = "".join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    return random_email + domain

email = generate_random_email()
print(email)
phone = "9818839688"


if is_valid_phone(phone):
    print("The phone number is valid")
else:
    print("The phone number is invalid")
if is_valid_email(email):
    print("The email is valid")
else:
    print("The email is invalid")

if not phone:
    print("Enter the phone number since its missing")
if not email:
    print("Enter the email since its missing")

#close the driver instance
driver.quit()