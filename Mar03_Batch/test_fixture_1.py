#pip install webdriver-manager


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    #ch_driver = webdriver.chrome(ChromeDriverManager("109.0.5414.119").install())
    ch_driver = webdriver.Chrome("/Users/mithunroy/Downloads/BrowserDrivers/chromedriver")
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass


class Test_Google_Chrome(Base_Chrome_Test):

    def test_google_app_chrome(self):
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(10)
        assert "Google" == self.driver.title
        self.driver.quit()

@pytest.mark.usefixtures("init_ff_driver")
class Base_FF_Test:
    pass


class Test_Docker_Firefox(Base_FF_Test):

    def test_docker_app_firefox(self):
        self.driver.get("https://www.docker.com")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "(//a[text()='Products'])[1]").click()
