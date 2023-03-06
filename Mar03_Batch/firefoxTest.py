from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Reusable import Common
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from webdriver_manager.firefox import GeckoDriverManager





class TestLocators:

    def initiateChromeDriver(self):

        global driver
        driver = webdriver.Firefox(executable_path="/Users/mithunroy/Downloads/BrowserDrivers/geckodriver")
        driver.maximize_window()
        #driver.get(Common.resdXMLAsPerNode("applicationURL"))
        driver.implicitly_wait(10)




    def handleStaticDropDown(self):
        try:
            driver.get("https://the-internet.herokuapp.com/dropdown")
            driver.implicitly_wait(10)
            select = Select(driver.find_element(By.ID, 'dropdown'))

            select.select_by_index(2)

            time.sleep(2)

          #  select.deselect_all()

            time.sleep(2)

            # select by visible text
            select.select_by_visible_text('Option 1')

            time.sleep(3)

           # select.deselect_all()

            time.sleep(2)

            # select by value
            select.select_by_value('2')
            time.sleep(3)
        except:
            print("Something went wrong")

    def handleStaticDropDown_By_Click(self):
        try:
            driver.get("https://www.techedtrainings.com/contact-us")
            driver.implicitly_wait(10)
            print(driver.title)
            driver.find_element(By.XPATH, "//select[@id='collection_comp-lcnkjfep']").click()
            time.sleep(3)

            # select by value
            driver.find_element(By.XPATH, "//div[text()='Software Engineering']").click()
            time.sleep(3)
        except:
            print("Something went wrong:handleStaticDropDown_By_Click")



    def handle_Text_Box(self):
        try:
            driver.get("https://infyni.com/register/")
            driver.implicitly_wait(10)
            driver.find_element(By.ID, "first_name").send_keys("MITHUN")
            driver.find_element(By.ID, "last_name").send_keys("ROY")

        except:
            print("Something went wrong:handle_Text_Box")


    def Auto_Select_Drop_Down(self):
        try:
            driver.get("https://www.pizzahut.co.in/")
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, "//input[@placeholder='Enter your location for delivery']").send_keys('Lulu Mall Bengaluru')
            time.sleep(5)
            driver.find_element(By.XPATH, "//div[text()='Lulu Mall Bengaluru']").click()
            time.sleep(5)

        except:
            print("Something went wrong:handle_Text_Box")


    def handle_check_box(self):
        try:
            driver.get("https://the-internet.herokuapp.com/checkboxes")
            driver.implicitly_wait(10)
            if driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]").is_selected():
                print("Checkbox 2 is selected ==== PASS")
            else:
                print("Checkbox 2 is not selected ==== FAIL")
            if not driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]").is_selected():
                print("Checkbox 1 is not selected ==== PASS")
                driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]").click()
                time.sleep(3)
            else:
                print("Checkbox 1 is not selected ==== FAIL")
        except:
            print("Something went wrong")


    def handle_radio_button_box(self):
        try:
            driver.get("https://mdbootstrap.com/docs/standard/forms/radio/")
            driver.implicitly_wait(10)
            if driver.find_element(By.XPATH, "//input[@id='flexRadioDefault2']").is_selected():
                print("Radio Button 2 is selected ==== PASS")
            else:
                print("Radio Button 2 is not selected ==== FAIL")
            if not driver.find_element(By.XPATH, "//input[@id='flexRadioDefault1']").is_selected():
                print("Radio Button 1 is not selected ==== PASS")
                driver.find_element(By.XPATH, "//input[@id='flexRadioDefault1']").click()
                time.sleep(3)
            else:
                print("Radio Button 1 is not selected ==== FAIL")
        except:
            print("Something went wrong:handle_radio_button_box")


    def frame_handle_selenium_python(self):
        try:
            driver.get("https://the-internet.herokuapp.com/iframe")
            driver.implicitly_wait(10)

            # Switch to Frame ...

            driver.switch_to.frame("mce_0_ifr")

            driver.find_element(By.XPATH, "//body[@id='tinymce']").clear()
            driver.find_element(By.XPATH, "//body[@id='tinymce']").send_keys('Lulu Mall Bengaluru')
            time.sleep(3)

            driver.get("https://the-internet.herokuapp.com/nested_frames")
            driver.implicitly_wait(10)


            # First Switch to default content ....

            driver.switch_to.default_content()

            # Switch to Frame ...

            driver.switch_to.frame("frame-left")

            driver.find_element(By.XPATH, "//body[contains(.,'LEFT')]").is_displayed()
            print('LEFT Text is Displayed ......')


        except:
            print("Something went wrong:frame_handle_selenium_python")

    def mouse_hover_then_click(self):
        try:
            driver.get("https://www.docker.com/")
            driver.implicitly_wait(10)
            ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "(//a[text()='Products'])[1]")).perform()
            time.sleep(3)
            driver.find_element(By.XPATH, "(//a[text()='Docker Pro'])[1]").click()
            driver.implicitly_wait(10)
            time.sleep(3)

        except:
            print("Something went wrong:mouse_hover_then_click")

    def scroll_to_element_then_click(self):
        try:
            driver.get("https://www.docker.com/")
            driver.implicitly_wait(10)
            ele = driver.find_element(By.XPATH, "//div/a[text()='Learn more']")
            ele.location_once_scrolled_into_view
            time.sleep(3)
            driver.find_element(By.XPATH, "//div/a[text()='Learn more']").click()
            time.sleep(3)

        except:
            print("Something went wrong:mouse_hover_then_click")

    def window_handle_selenium_python(self):
        try:
            driver.get("https://www.docker.com/")
            driver.implicitly_wait(10)

            driver.find_element(By.XPATH, "//img[@alt='twitter logo']").click()
            driver.implicitly_wait(10)
            handles = driver.window_handles
            size = len(handles)
            parent_handle = driver.current_window_handle
            for x in range(size):
                if handles[x] != parent_handle:
                    driver.switch_to.window(handles[x])
                    print(driver.title)
                    driver.close() # Closing current TAB
                    break

            driver.switch_to.window(parent_handle) # Moving back to Parent Window

            driver.find_element(By.XPATH, "(//a[text()='Sign In'])[1]").click()
            driver.implicitly_wait(10)

        except:
            print("Something went wrong:mouse_hover_then_click")


    def javascripts_alert_handle(self):
        try:
            driver.get("https://the-internet.herokuapp.com/javascript_alerts")
            driver.implicitly_wait(10)

            # First Alert ...
            driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
            time.sleep(3)
            # create alert object
            alert = Alert(driver)
            print(alert.text)
            alert.accept()
            time.sleep(3)
            driver.find_element(By.XPATH, "//p[text()='You successfully clicked an alert']").is_displayed()

            # Second Alert ...
            driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
            time.sleep(3)
            # create alert object
            alert = Alert(driver)
            print(alert.text)
            alert.dismiss()
            time.sleep(3)
            driver.find_element(By.XPATH, "//p[text()='You clicked: Cancel']").is_displayed()

            # Third Alert ...
            driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
            time.sleep(3)
            # create alert object
            alert = Alert(driver)
            print(alert.text)
            alert.send_keys('Mithun')
            alert.accept()
            time.sleep(3)
            driver.find_element(By.XPATH, "//p[text()='You entered: Mithun']").is_displayed()



        except:
            print("Something went wrong:mouse_hover_then_click")



    def tearDown(self):

            driver.quit()


obj = TestLocators()
obj.initiateChromeDriver()
#obj.handleStaticDropDown()
#obj.handleStaticDropDown_By_Click()
#obj.handle_Text_Box()
#obj.Auto_Select_Drop_Down()
#obj.handle_check_box()
#obj.handle_radio_button_box()
#obj.frame_handle_selenium_python()
#obj.mouse_hover_then_click()
#obj.scroll_to_element_then_click()
#obj.window_handle_selenium_python()
obj.javascripts_alert_handle()

obj.tearDown()



