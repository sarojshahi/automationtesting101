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
full_name = driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
email_field = driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
phone = driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
subject = driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
any_queries = driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))


#passing the value in the variable
name="Saroj Shahi"
email="sarojshaic4@gmail.com"
phoneno="9818839asv"
subjectarea="Quality Assurance"
anyqueries="Yes Please"

time.sleep(2)

#check the validity of the email
if is_valid_email(email):
    print("The given email is valid")
else:
    print("The given email is invalid")


#Sending values to the forms
full_name.send_keys(name)
email_field.send_keys(email)
phone.send_keys(phoneno)
subject.send_keys(subjectarea)
any_queries.send_keys(anyqueries)

time.sleep(2)

#check the validity of the phone
if is_valid_phone(phoneno):
    print("The given number is valid")
else:
    print("the given number is invalid")


#close the web driver instance
driver.quit()
print("Email Validation is executed successfully")