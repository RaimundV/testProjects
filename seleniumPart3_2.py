#Practice 3 task 2
from selenium.webdriver.support import expected_conditions as EC
import unittest
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestAbs(unittest.TestCase):
    def testForm(self):
        browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
        browser.get("http://suninjuly.github.io/registration1.html")

        firstElem = browser.find_elements_by_class_name("first")
        secondElem = browser.find_elements_by_class_name("second")
        thirdElem = browser.find_elements_by_class_name("third")

        self.assertEqual(2, len(firstElem), "has to be 2 first class elements")
        self.assertEqual(2, len(secondElem), "has to be 2 second class elements")
        self.assertEqual(1, len(thirdElem), "has to be 1 third class elements")
        browser.close()
    def testForm2(self):
        browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
        browser.get("http://suninjuly.github.io/registration2.html")

        firstElem = browser.find_elements_by_class_name("first")
        secondElem = browser.find_elements_by_class_name("second")
        thirdElem = browser.find_elements_by_class_name("third")

        self.assertEqual(2, len(firstElem), "has to be 2 first class elements")
        self.assertEqual(2, len(secondElem), "has to be 2 second class elements")
        self.assertEqual(1, len(thirdElem), "has to be 1 third class elements")
        browser.close()

if __name__ == "__main__":
    unittest.main()
