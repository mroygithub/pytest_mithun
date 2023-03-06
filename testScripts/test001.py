from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLocators:

    def IdentifyLocators(self):

        driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
        driver.implicitly_wait(10)
        driver.get("https://www.google.com")


        # Do Some Testing ...


        driver.quit


obj = TestLocators()
obj.IdentifyLocators()


