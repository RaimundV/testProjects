#Practice 1
from selenium import webdriver
import time

link = "https://www.tribalwars.net/en-dk/page/new"
try:
    browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
    browser.get(link)
    input1 = browser.find_element_by_name("register_username")
    input1.send_keys("test")

    input2 = browser.find_element_by_name("register_password")
    input2.send_keys("testrasda123")
    time.sleep(1)
    inputerror = browser.find_element_by_class_name("suggested-name")
    if inputerror.text != "":
        input1.send_keys(inputerror.text)
    input3 = browser.find_element_by_name("register_email")
    input3.send_keys("lol@gmail.com")
    input4 = browser.find_element_by_name("terms")
    input4.click()

    input5 = browser.find_element_by_class_name("btn-register")
    input5.click()

finally:
    time.sleep(5)
    browser.quit()