from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class startExecution:

    def googleTesting(self):

        driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
        driver.implicitly_wait(10)
        driver.get("https://google.com")
        driver.maximize_window()

        I_AmFeeling_lcy = driver.find_element(By.NAME, "btnI")
        I_AmFeeling_lcy.is_displayed()
        print("Google Page I_AmFeeling_lcy is getting displayed ...")
        I_AmFeeling_lcy.click()

        google_logo = driver.find_element(By.CLASS_NAME, "lnXdpd")
        google_logo.is_displayed()
        print("Google Page logo is getting displayed ...")

        search_in_google = driver.find_element(By.NAME, "q")
        search_in_google.send_keys("Robot Framework")
        sleep(5)
        print("Google Page logo is getting displayed ...")

        driver.find_element(By.XPATH, "//a[text()='Contact Us']").click()

        driver.quit()
        print("Google Browser has launched successfully and closed ....")
    
    def techedtrainingsTesting(self):
        driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
        driver.implicitly_wait(10)
        driver.get("https://techedtrainings.com/contact/")
        driver.maximize_window()

        submitbuttonpro = driver.find_element(By.XPATH, "//button[contains(.,'submit')]")
        print("The font Family of Submit button is ==> :"+submitbuttonpro.value_of_css_property("font-family"))
        print("The font Family of Submit button is ==> :" + submitbuttonpro.value_of_css_property("color"))
        print("The font Family of Submit button is ==> :" + submitbuttonpro.value_of_css_property("background"))





obj = startExecution()
obj.techedtrainingsTesting()