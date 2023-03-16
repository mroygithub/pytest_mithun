from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Reusable import Common
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager





class TestLocators:

    def initiateChromeDriver(self):

        global driver
        #driver = webdriver.Chrome(Common.resdXMLAsPerNode("chromepath"))
        #driver.get(Common.resdXMLAsPerNode("applicationURL"))
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(Common.resdXMLAsPerNode("URL"))
        driver.implicitly_wait(10)
        driver.maximize_window()

        # Validate Page Title

        runTitle = driver.title

        if runTitle == Common.resdXMLAsPerNode("title"):
            print("Application Title is Correct.................PASS")
        else:
            print("Application Title is Incorrect.............FAIL")





    def validateWebElementPresent(self):
        try:



            time.sleep(3)
        except:
            print("Something went wrong")





    def tearDown(self):

            driver.quit()


obj = TestLocators()
obj.initiateChromeDriver()




obj.tearDown()



