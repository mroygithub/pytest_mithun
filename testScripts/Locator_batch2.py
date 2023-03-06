from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Reusable import Common


class TestLocators:

    def IdentifyLocators(self):

        driver = webdriver.Chrome(Common.resdXMLAsPerNode("chromepath"))
        driver.get(Common.resdXMLAsPerNode("applicationURL"))
        driver.implicitly_wait(10)

        # Get the Count of primary menu ....

        primarymenu = driver.find_elements(By.XPATH, "(//div[@class='container'])[2]/div/div/div/div/ul/li/a")
        print(len(primarymenu))


        driver.find_element(By.XPATH, Common.validatePrimaryMenusByXpath("Home")).is_displayed()
        print(Common.validatePrimaryMenusByXpath("Home"))
        driver.find_element(By.XPATH, Common.validatePrimaryMenusByXpath("Courses")).is_displayed()
        print(Common.validatePrimaryMenusByXpath("Courses"))
        driver.find_element(By.XPATH, Common.validatePrimaryMenusByXpath("Contact")).is_displayed()
        print(Common.validatePrimaryMenusByXpath("Contact"))

        # Do Some Testing ...


        driver.quit

obj = TestLocators()
obj.IdentifyLocators()



