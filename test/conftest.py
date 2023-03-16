import sys
sys.path.append('/Users/mithunroy/PycharmProjects/simplePythonSelenium')
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import json
import time


@pytest.fixture()
def jsonData():
    with open('../testData/testData.json') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()

@pytest.fixture()
def browser(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.instance.driver = driver
    driver.maximize_window()

    yield driver

    driver.close()
