from testScripts.Test1 import add
from selenium import webdriver


def add1():
    driver = webdriver.Chrome("/Users/mithunroy/Downloads/chromedriver")
    driver.implicitly_wait(10)
    driver.get("https://infyni.com")
    driver.maximize_window()
    driver.close()


print("Welome")
add()
add1()




