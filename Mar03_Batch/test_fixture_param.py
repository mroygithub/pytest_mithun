#pip install webdriver-manager


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("init_driver")
class Base_Test:
    pass


class Test_Google(Base_Test):

    def test_google_app(self):
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(10)
        assert "Google" == self.driver.title, "Title is invalid"
        self.driver.quit()

