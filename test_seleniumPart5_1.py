#Practice 4 task 1
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class TestForms():

    @pytest.fixture(scope="function")
    def openUrl1(self):
        openUrl1 = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
        wait = WebDriverWait(openUrl1, 3)
        openUrl1.get("http://suninjuly.github.io/registration1.html")
        yield openUrl1
        openUrl1.close()

    @pytest.fixture(scope="function")
    def openUrl2(self):
        openUrl2 = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
        wait = WebDriverWait(openUrl2, 3)
        openUrl2.get("http://suninjuly.github.io/registration2.html")
        yield openUrl2
        openUrl2.close()

    def testForm(self, openUrl1):

        firstElem = openUrl1.find_elements_by_class_name("first")
        secondElem = openUrl1.find_elements_by_class_name("second")
        thirdElem = openUrl1.find_elements_by_class_name("third")

        assert 2 == len(firstElem), "has to be 2 first class elements"
        assert 2 == len(secondElem), "has to be 2 second class elements"
        assert 1 == len(thirdElem), "has to be 1 third class elements"


    def testForm2(self, openUrl2):

        firstElem = openUrl2.find_elements_by_class_name("first")
        secondElem = openUrl2.find_elements_by_class_name("second")
        thirdElem = openUrl2.find_elements_by_class_name("third")

        assert 2 == len(firstElem), "has to be 2 first class elements"
        assert 2 == len(secondElem), "has to be 2 second class elements"
        assert 1 == len(thirdElem), "has to be 1 third class elements"

