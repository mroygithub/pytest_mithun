# Implementation of Selenium test automation for this Selenium Python Tutorial
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_lambdatest_todo_app():

    chrome_driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")

    chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
    chrome_driver.maximize_window()

    chrome_driver.find_element(By.NAME, "li1").click()
    chrome_driver.find_element(By.NAME, "li2").click()

    title = "Sample page - lambdatest.com"
    assert title == chrome_driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = chrome_driver.find_element(By.ID, "sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(5)
    chrome_driver.close()