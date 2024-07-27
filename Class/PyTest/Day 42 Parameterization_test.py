import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture()
#function to set up chrome driver manager
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    #yield the driver
    yield driver
    #chlose the driver instance
    driver.quit()

#function for parameterization
@pytest.mark.parametrize("username ")