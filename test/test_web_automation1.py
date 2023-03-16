import sys
sys.path.append('/Users/mithunroy/PycharmProjects/simplePythonSelenium')
from pageObject.homepage import HomePage
from htmlLocators import google
from Reusable import Common
import pytest



class TestUi1:

    def test_ui_google_search(self, browser, jsonData):

        browser.get(jsonData['url'])
        demo = HomePage(browser)
        demo.search_in_google(google.google_search_box(), Common.resdXMLAsPerNode("googletext"))
        demo.google_logo_validation(google.google_logo())

    def test_ui_google_search_k(self, browser, jsonData):

        browser.get(jsonData['url1'])
        demo = HomePage(browser)