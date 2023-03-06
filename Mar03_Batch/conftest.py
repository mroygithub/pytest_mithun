
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



def pytest_addoption(parser):
    #parser.addoption("--driver_path", action="store", help="input driver_path")
    parser.addoption("--url", action="store", help="input url")
    parser.addoption("--browser", action="store", help="input browser")

@pytest.fixture
def params(request):
    params = {}
    #params['driver_path'] = request.config.getoption('--driver_path')
    params['url'] = request.config.getoption('--url')
    params['browser'] = request.config.getoption('--browser')
    return params


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    print("=========>"+request.param)
    if request.param =="chrome":
        #ch_driver = webdriver.chrome(ChromeDriverManager("109.0.5414.119").install())
        web_driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")

    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = web_driver
    yield
    web_driver.close()