#Mithuns-MacBook-Air-2:Mar03_Batch mithunroy$ py.test test_param_data_login.py --html=A.html



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.common.by import By
import time



@pytest.mark.usefixtures("init_driver")
class Base_Test_Parem:
    pass


class Test_To_Login_Page_With_Different_Test_data(Base_Test_Parem):

    @pytest.mark.parametrize(

        "username , password",
        [
            ("test001@gmail.com", "password1"),
            ("test002@gmail.com", "password1"),
            ("test003@gmail.com", "password1"),
            ("test004@gmail.com", "password1"),
            ("test005@gmail.com", "password1")
        ]
    )
    def test_login_scenario_webucator(self, username, password):

        self.driver.get("https://www.webucator.com/account/login/")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, "login").clear()
        self.driver.find_element(By.NAME, "login").send_keys(username)
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys(password)
        time.sleep(3)


