from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjectModel import HomePage
from PageObjectModel import SignInPage
from Reusable import Reusable



class TestWebu:

        def launchwebucatorapplication(self):

            global driver
            driver = webdriver.Chrome(Reusable.readXmlTestData("chromePath"))
            driver.implicitly_wait(10)
            driver.get(Reusable.readXmlTestData("url"))
            driver.maximize_window()

        def dowebucatorHomepageTesting(self):

            """
            1. Click on Webucator Logo
            2. Validate the URL?
            3. Validate Page Title..
            4. Check for 'Technical & Business Training' header
            4. Check Sign In Button
            5. Click On Sign In Button
            6. Validate user is navigating to Sign In Page
            """

            logo = driver.find_element(By.XPATH, HomePage.logo_xpath())
            logo.click()
            driver.implicitly_wait(10)
            if driver.current_url == Reusable.readXmlTestData("url"):
                print("After Clicking on Logo , it is navigating to Home Page==>"+"PASS")
            if driver.title == Reusable.readXmlTestData("pageTitle"):
                print("After Clicking on Logo , it is showing correct Page==>" + "PASS")

            if driver.find_element(By.XPATH, HomePage.TechnicalBusinessTraining_xpath()).is_displayed():
                print("TechnicalBusinessTraining Header is present in Home Page==>" + "PASS")


        def dowebucatorLoginpageTesting(self):

            if driver.find_element(By.XPATH, HomePage.SignIn_xpath()).is_displayed():
                print("Sign In button is present in Home Page==>" + "PASS")

            # Click on SignIn btn...

            driver.find_element(By.XPATH, HomePage.SignIn_xpath()).click()
            driver.implicitly_wait(10)

            if driver.find_element(By.XPATH, SignInPage.SignInHeader_xpath()).is_displayed():
                print("User successfully navigated to Sign In Page==>" + "PASS")


        def dowebucator_Quit(self):

            driver.quit()
            print("Webucator Application is Closed")


obj = TestWebu()
obj.launchwebucatorapplication()
obj.dowebucatorHomepageTesting()
obj.dowebucatorLoginpageTesting()
obj.dowebucator_Quit()