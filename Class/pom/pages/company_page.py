#QA TESTING

from selenium.webdriver.common.by import By

class Company:
    def __init__(self,driver):
         self.driver = driver
    def open_page(self,url):
         self.driver.get(url)

    def scroll_window(self):
        target_y = 600
        scroll_distance = 100
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
