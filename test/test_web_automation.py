import pytest
import sys
sys.path.append('/Users/mithunroy/PycharmProjects/simplePythonSelenium')
from pageObject.homepage import HomePage
from htmlLocators import google
from Reusable import Common


@pytest.mark.usefixtures("setup")

class TestUi:

    def test_ui_google(self, jsonData):

        self.driver.get(jsonData['url'])
        demo = HomePage(self.driver)
        demo.search_in_google(google.google_search_box(), Common.resdXMLAsPerNode("googletext"))
        demo.google_logo_validation(google.google_logo())

    @pytest.mark.smoke
    def test_ui_google_sm(self, jsonData):

        self.driver.get(jsonData['url1'])
        demo = HomePage(self.driver)