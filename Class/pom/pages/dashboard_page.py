#This is a page object model for dashboard page
#import necessary modules
from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self,driver):
        self.driver = driver
        self.about_yourself_link = By.XPATH,"//a[normalize-space()='About Yourself']"
        self.articles_link = By.XPATH,"//a[normalize-space()='Articles']"
        self.contact_me_link = By.XPATH,"//a[normalize-space()='Contact Me']"
        self.qa_testing_link = By.XPATH,"//a[normalize-space()='QA Testing']"
        self.company_link = By.XPATH,"//a[normalize-space()='Company']"

    def open_page(self,url):
        self.driver.get(url)

    def return_home(self):
        self.driver.get("https://sagar-test-qa.vercel.app/dashboard.html")

    def open_about_yourself(self):
        self.driver.find_element(*self.about_yourself_link).click()

    def open_articles(self):
        self.driver.find_element(*self.articles_link).click()

    def open_contact_me(self):
        self.driver.find_element(*self.contact_me_link).click()

    def open_qa_testing(self):
        self.driver.find_element(*self.qa_testing_link).click()

    def open_company(self):
        self.driver.find_element(*self.company_link).click()


