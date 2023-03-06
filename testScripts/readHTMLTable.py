from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from Reusable import Reusable
from PageObjectModel import SignUpPage

class ReadHTML:

    def testautomationpractice(self):

        global driver
        driver = webdriver.Chrome("/Users/mithunroy/Desktop/deleteit/chromedriver")
        driver.implicitly_wait(10)
        driver.get("https://testautomationpractice.blogspot.com/")
        driver.maximize_window()

        #   read HTML Table ...

        #   Get total row count?

        print("Total Table Row Count is ==> "+str
        (len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))))

        #   Get Total Column Count?

        print("Total Table Column Count is ==> " + str(
            len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))))
        
        #   Get Author , Subject , Price as per the BookName

        print("If my BookName is"+" "+ Reusable.readXmlTestData("bookName")+" Then  Auther Name is  ==> " +
            driver.find_element(By.XPATH, SignUpPage.autherName(Reusable.readXmlTestData("bookName"))).text)

        print("If my BookName is"+" "+ Reusable.readXmlTestData("bookName") + " Then  Subject Name is  ==> " +
              driver.find_element(By.XPATH, SignUpPage.SubjectName(Reusable.readXmlTestData("bookName"))).text)

        print("If my BookName is"+" "+ Reusable.readXmlTestData("bookName") + " Then  Price Name is  ==> " +
              driver.find_element(By.XPATH, SignUpPage.Pricing(Reusable.readXmlTestData("bookName"))).text)




    def testtheradiobutton(self):

        # Make sure Male radio button is not selected ...

        driver.get("https://intellipaat.com/signin/")
        driver.implicitly_wait(10)

        #    First Check Remember Me check box is not checked by default ..

        check_box = driver.find_element(By.NAME, "rememberme")
        if not check_box.is_selected():
            print("Remember Me check box is not selected by deefault ...")


        #   Check Remember Me check box

        check_box.click()
        sleep(2)


        # Remember Me check box is selected

        if check_box.is_selected():
            print("Remember Me check box is selected once we click on it ...")

    def checkLinks(self):

        # Make sure Male radio button is not selected ...

        driver.get("https://intellipaat.com")
        driver.implicitly_wait(10)
        elems = driver.find_elements(By.XPATH, "//a")
        for a in elems:
            #print(a.text)
            if a.text == "Download Transition Handbook":
                print(a.text)
                break


        driver.find_element(By.XPATH, SignUpPage.
                            intellipathfootersection(Reusable.
                                                     readXmlTestData("intellipathfooter1").split(",")[0]
                                                     , Reusable.readXmlTestData("intellipathfooter1").split(",")[1])).is_displayed()
        driver.find_element(By.XPATH, SignUpPage.
                            intellipathfootersection(Reusable.
                                                     readXmlTestData("intellipathfooter2").split(",")[0]
                                                     , Reusable.readXmlTestData("intellipathfooter2").split(",")[
                                                         1])).is_displayed()


        driver.quit()

hml = ReadHTML()
hml.testautomationpractice()
hml.testtheradiobutton()
hml.checkLinks()
