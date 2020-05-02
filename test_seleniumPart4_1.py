#Practice 4 task 1
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def default_init(request):
    browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
    request.cls.driver = browser
    yield
    browser.close()

@pytest.mark.usefixtures("default_init")
class testBase:
    pass

class TestForms(testBase):

    def testForm(self):
        self.driver.get("http://suninjuly.github.io/registration1.html")
        firstElem = self.driver.find_elements_by_class_name("first")
        secondElem = self.driver.find_elements_by_class_name("second")
        thirdElem = self.driver.find_elements_by_class_name("third")

        assert 2 == len(firstElem), "has to be 2 first class elements"
        assert 2 == len(secondElem), "has to be 2 second class elements"
        assert 1 == len(thirdElem), "has to be 1 third class elements"


    def testForm2(self):
        self.driver.get("http://suninjuly.github.io/registration2.html")
        firstElem = self.driver.find_elements_by_class_name("first")
        secondElem = self.driver.find_elements_by_class_name("second")
        thirdElem = self.driver.find_elements_by_class_name("third")

        assert 2 == len(firstElem), "has to be 2 first class elements"
        assert 2 == len(secondElem), "has to be 2 second class elements"
        assert 1 == len(thirdElem), "has to be 1 third class elements"

