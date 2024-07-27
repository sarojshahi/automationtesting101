# login page
import time

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "username")
        self.password_textbox = (By.ID, "password")
        self.login_button = By.XPATH, "//button[normalize-space()='Login']"

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_alert_text_and_accept(self):
        try:
            alert=self.driver.switch_to.alert
            alert_text=alert.text
            alert.accept()
            return alert_text
        except:
            return None

    def is_dashboard_present(self):
        time.sleep(2)
        return "Welcome to the Dashboard" in self.driver.page_source