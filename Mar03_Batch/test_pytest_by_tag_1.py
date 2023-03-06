
#MMithuns-MacBook-Air-2:Mar03_Batch mithunroy$ py.test -m regression

import pytest
from selenium.webdriver.common.by import By
import sys
sys.path.append('/Users/mithunroy/PycharmProjects/simplePythonSelenium')
from selenium import webdriver
from Reusable import Common


@pytest.mark.smoke
def test_google_1():


        driver = webdriver.Chrome(Common.resdXMLAsPerNode('chromepath'))
        driver.maximize_window()
        driver.get("https://www.google.com")
        driver.implicitly_wait(10)
        assert "Google" == driver.title
        driver.quit()

@pytest.mark.regression
def test_docker_1():


        driver = webdriver.Chrome(Common.resdXMLAsPerNode('chromepath'))
        driver.maximize_window()
        driver.get("https://www.docker.com")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "(//a[text()='Products'])[1]").click()
        driver.quit()

@pytest.mark.sanity
def test_Facebook_1():


        driver = webdriver.Chrome(Common.resdXMLAsPerNode('chromepath'))
        driver.maximize_window()
        driver.get("https://www.facebook.com")
        driver.implicitly_wait(10)
        assert "Facebook – log in or sign up" == driver.title
        driver.quit()

@pytest.mark.smoke
def test_twitter_1():


        driver = webdriver.Chrome(Common.resdXMLAsPerNode('chromepath'))
        driver.maximize_window()
        driver.get("https://www.twitter.com")
        driver.implicitly_wait(10)
        assert "https://twitter.com/" == driver.current_url
        driver.quit()