#Practice 3 task 1
from selenium.webdriver.support import expected_conditions as EC

import numpy as np
from selenium import webdriver
import time
import numpy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
    browser.get(link)

    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button.click()

    input2 = browser.find_element_by_id("input_value")

    value = np.log(abs(12 * np.sin(int(input2.text))))

    input3 = browser.find_element_by_id("answer")
    input3.send_keys(str(value))

    input4 = browser.find_element_by_id("solve")
    input4.click()

finally:
    time.sleep(5)
    browser.quit()