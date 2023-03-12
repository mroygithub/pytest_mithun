# Python code to demonstrate working of unittest
# Appium With Python
# Android Native App with Appium Python
import unittest
from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy


class TestMobileChrome(unittest.TestCase):
    desired_caps = {
        "deviceName": "Samsung",
        "platformName": "Android",
        "version": "9.0",
        "udid": "11f2b948",
        "app": "/Users/mithunroy/Downloads/naukri-com-17-1.apk"
    }

    # Android Native App in Real Device using Chrome

    def setUp(self):
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
        driver.update_settings({"waitForIdleTimeout": 500})

        # Validate Later/Settings Cancel button ...
    def skip_settings(self):
        try:
            time.sleep(5)
            self.assertTrue(driver.find_element(AppiumBy.ID,
                                                "naukriApp.appModules.login:id/ssa_cancel_textview").is_displayed())
            driver.find_element(AppiumBy.ID,
                                    "naukriApp.appModules.login:id/ssa_cancel_textview").click()
            time.sleep(5)
            print('Later button closed successfully')

        except:
            print('Setting option skipped ...')
    '''
    # Validate Get Started on Naukri Screen ...
    def test_002_Get_Started_Naukri_Screen(self):
        try:
            self.skip_settings()
            time.sleep(5)
            self.assertTrue(driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Get started on Naukri']").is_displayed())
            self.assertTrue(
                driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/textViewNormalLogin").is_displayed())
            self.assertTrue(driver.find_element(AppiumBy.XPATH,
                                                "//android.widget.TextView[@text='Already have an account?']").is_displayed())
            self.assertTrue(
                driver.find_element(AppiumBy.ID, "naukriApp.appModules.login:id/textViewLogin").is_displayed())
            self.assertTrue(driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textViewFirst']").is_displayed())
            self.assertTrue(driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textViewSecond']").is_displayed())
            print('Get Started on Naukri secton is PASS')

        except:
            print('Get Started on Naukri secton is FAIL')

            # Validate Get Started on Naukri Screen ...
    '''
    def test_003_SearchJob_Flow(self):
        try:

            self.skip_settings()
            time.sleep(5)
            driver.press_keycode(4)
            time.sleep(2)

            driver.find_element(AppiumBy.ID,
                                                "naukriApp.appModules.login:id/autoCompleteKeyskills").send_keys("automation testing")
            driver.find_element(AppiumBy.ID,
                                "naukriApp.appModules.login:id/autoCompleteLocation").send_keys("Bangalore/Bengaluru")
            time.sleep(2)

            driver.find_element(AppiumBy.ID,
                                "naukriApp.appModules.login:id/tv_search_jobs").click()

            time.sleep(8)

            skills = driver.find_element(AppiumBy.XPATH,
                                                "(//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textViewDesignation'])[1]").get_attribute('text')

            print(skills)
            skills = driver.find_element(AppiumBy.XPATH,
                                         "(//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textViewDesignation'])[2]").get_attribute(
                'text')

            print(skills)
            skills = driver.find_element(AppiumBy.XPATH,
                                         "(//android.widget.TextView[@resource-id='naukriApp.appModules.login:id/textViewDesignation'])[3]").get_attribute(
                'text')

            print(skills)

            print('Jon Search Flow is Working Fine ..... PASS')

        except:
            print('Job Search Flow is Failing  FAIL')




    # Quiting the App
    def tearDown(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()