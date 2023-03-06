#pip install pytest-xdist
#Mithuns-MacBook-Air-2:Mar03_Batch mithunroy$ py.test -n 2 test_parallel_Execution.py
import pytest
from selenium.webdriver.common.by import By
import sys
sys.path.append('/Users/mithunroy/PycharmProjects/simplePythonSelenium')
from selenium import webdriver
from Reusable import Common



def test_google():


        driver = webdriver.Chrome(Common.resdXMLAsPerNode('chromepath'))
        driver.maximize_window()
        driver.get("https://www.google.com")
        driver.implicitly_wait(10)
        assert "Google" == driver.title
        driver.quit()


def test_docker():


        #driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
        driver = webdriver.Chrome(Common.resdXMLAsPerNode('chromepath'))
        driver.maximize_window()
        driver.get("https://www.docker.com")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//a[text()='Products'])[1]").click()
        driver.quit()


def test_Facebook():


        #driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
        driver = webdriver.Chrome(Common.resdXMLAsPerNode('chromepath'))
        driver.maximize_window()
        driver.get("https://www.facebook.com")
        driver.implicitly_wait(10)
        assert "Facebook – log in or sign up" == driver.title
        driver.quit()


def test_twitter():


        #driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
        driver = webdriver.Chrome(Common.resdXMLAsPerNode('chromepath'))
        driver.maximize_window()
        driver.get("https://www.twitter.com")
        driver.implicitly_wait(10)
        assert "https://twitter.com/" == driver.current_url
        driver.quit()