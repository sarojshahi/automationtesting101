# #import necessary modules:
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import pytest
# from Class.pom.pages.login_page import LoginPage
#
# @pytest.fixture()
# def driver():
#     # set the chromedriver manager
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.implicitly_wait(10)
#     #yield the driver
#     yield driver
#     #close the driver
#     driver.quit()
#
# @pytest.mark.parametrize("username,password",[
#     ("TestQA","password"), #valid username and password
#     ("invalid","password"), #invalid username and password
#     ("1","1"), #invalid username and password
#     ("a",""), #invalid username and password
# ])
#
# def test_login(driver,username,password):
#     login_page=LoginPage(driver)
#     login_page.open_page("https://sagar-test-qa.vercel.app/")
#     time.sleep(1)
#     login_page.enter_username(username)
#     time.sleep(1)
#     login_page.enter_password(password)
#     time.sleep(1)
#     login_page.click_login()
#     time.sleep(1)
#
#     alert_text=login_page.get_alert_text_and_accept()
#     if alert_text and "Invalid username or password" in alert_text:
#         print(f"Invalid username or password for {username}")
#     else:
#         if login_page.is_dashboard_present():
#             print(f"Successful login for {username}")
#         else:
#             print(f"Unexpected error or login failed for {username}")


#import all the modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from Class.pom.pages.login_page import LoginPage
from Class.pom.pages.dashboard_page import DashboardPage
from Class.pom.pages.aboutus_page import AboutUsPage
from Class.pom.pages.articles_page import ArticlesPage
from Class.pom.pages.contact_me_page import ContactMe
from Class.pom.pages.qa_testing_page import QaTesting
from Class.pom.pages.company_page import Company


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    yield driver
    driver.quit()

@pytest.mark.parametrize("username,password",[
    ("TestQA","password"),
    ("TestQA","pass"),
    ("QA","password"),
    ("123","abc"),
    ])

def test_login(driver,username, password):
    login_page = LoginPage(driver)
    login_page.open_page("https://sagar-test-qa.vercel.app/")
    driver.maximize_window()
    time.sleep(2)
    login_page.enter_username(username)
    time.sleep(1)
    login_page.enter_password(password)
    time.sleep(1)
    login_page.click_login()
    time.sleep(3)

    alert_text = login_page.check_alert_and_accept()
    if alert_text and "Invalid username or password" in alert_text:
        print("Invalid username or password")
    else:
        if login_page.is_dashboard_active():
            print("You have successfully logged in")
        else:
            print("Unexpected Error or Invalid user request")

def test_dashboard(driver):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open_page("https://sagar-test-qa.vercel.app/dashboard.html")
    driver.maximize_window()
    time.sleep(3)
    print("Your Dashboard Page Testing is runnning successfully")


def test_aboutus(driver):
    about_us = AboutUsPage(driver)
    about_us.open_page("https://sagar-test-qa.vercel.app/about.html")
    time.sleep(1)
    about_us.enter_fullname("Saroj")
    time.sleep(1)
    about_us.enter_phone("9818839688")
    time.sleep(1)
    about_us.enter_email("saroj@gmail.com")
    time.sleep(1)
    about_us.enter_hobby("Listening to music")
    time.sleep(1)
    about_us.click_submit()
    time.sleep(2)

    print("The about us page has been tested successfully")

def test_articles(driver):
    articles = ArticlesPage(driver)
    articles.open_page("https://sagar-test-qa.vercel.app/articles.html")
    driver.maximize_window()
    time.sleep(1)
    articles.scroll_window()
    time.sleep(1)

    print("The Articles Page has been tested successfully")


def test_contact_me(driver):
    contact = ContactMe(driver)
    contact.open_page("https://sagar-test-qa.vercel.app/contact.html")
    driver.maximize_window()
    time.sleep(1)
    contact.enter_name("Saroj Shahi")
    time.sleep(1)
    contact.enter_email("saroj@gmail.com")
    time.sleep(1)
    contact.enter_message("This is a test")
    time.sleep(1)
    contact.click_send_message()
    time.sleep(1)

    print("Your contact me page has been tested successfully")

def test_qa_testing(driver):
    qa_testing = QaTesting(driver)
    qa_testing.open_page("https://sagar-test-qa.vercel.app/qa.html")
    driver.maximize_window()
    time.sleep(1)
    qa_testing.scroll_window()
    time.sleep(1)

def test_company(driver):
    company = Company(driver)
    company.open_page("https://sagar-test-qa.vercel.app/company.html")
    driver.maximize_window()
    time.sleep(1)
    company.scroll_window()
    time.sleep(1)