from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:

    def add(self):

        driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
        driver.get("https://infyni.com/register/")
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "first_name").send_keys("MITHUN")
        driver.find_element(By.ID, "last_name").send_keys("ROY")
        driver.close()


obj = Test()
obj.add()