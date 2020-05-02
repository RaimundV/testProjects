#Practice 2 task 2
import numpy as np
from selenium import webdriver
import time
import numpy

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
    browser.get(link)

    input1 = browser.find_element_by_class_name("trollface")# btn btn-primary")
    input1.click()

    new_browser = browser.window_handles[1]
    browser.switch_to.window(new_browser)
    input2 = browser.find_element_by_id("input_value")

    value = np.log(abs(12 * np.sin(int(input2.text))))

    input3 = browser.find_element_by_id("answer")
    input3.send_keys(str(value))
    input3.click()

    input4 = browser.find_element_by_class_name("btn")
    input4.click()

finally:
    time.sleep(5)
    browser.quit()