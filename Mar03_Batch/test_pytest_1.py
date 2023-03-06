
import pytest
from selenium.webdriver.common.by import By
import sys
sys.path.append('/Users/mithunroy/PycharmProjects/simplePythonSelenium')
from selenium import webdriver
from Reusable import Common



def test_first_case_selenium_with_pytest():


        #driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
        driver = webdriver.Chrome(Common.resdXMLAsPerNode('chromepath'))
        driver.maximize_window()
        driver.get("https://www.google.com")
        driver.implicitly_wait(10)
        assert "Google" == driver.title
        driver.quit()


def test_first_case_selenium_with_pytest_docker():


        #driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
        driver = webdriver.Chrome(Common.resdXMLAsPerNode('chromepath'))
        driver.maximize_window()
        driver.get("https://www.docker.com")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//z[text()='Products'])[1]").click()
        driver.quit()
