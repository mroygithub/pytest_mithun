# Mithuns-MacBook-Air-2:Mar03_Batch mithunroy$ py.test play.py --url https://www.webucator.com --browser chrome --html=A.html


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from Reusable import Common
import sys
sys.path.append('/Users/mithunroy/PycharmProjects/simplePythonSelenium')


def test_Print_All_Links_using_Headless_mode(params):
    if params["browser"] == 'chrome':
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(Common.resdXMLAsPerNode("chromepath"), options=options)
        driver.get(params["url"])
        print('Done!')
        all_link = driver.find_elements(By.XPATH, "//a")
        for lnk in all_link:
            print(lnk.text)
            print(lnk.get_attribute('href'))
        driver.quit()

    if params["browser"] == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        driver.get(params["url"])
        print('Done!')
        all_link = driver.find_elements(By.XPATH, "//a")
        for lnk in all_link:
            print(lnk.text)
            print(lnk.get_attribute('href'))
        driver.quit()
