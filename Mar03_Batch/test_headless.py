#Mithuns-MacBook-Air-2:Mar03_Batch mithunroy$ py.test play.py --url https://www.webucator.com --browser chrome --html=A.html


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options





def test_Print_All_Links_using_Headless_mode(params):
    if params["browser"]=='chrome':
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver", options=options)
        driver.get(params["url"])
        print('Done!')
        driver.quit()

    if params["browser"]=='firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        driver.get(params["url"])
        print('Done!')
        driver.quit()
