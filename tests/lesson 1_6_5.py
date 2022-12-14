import math

from selenium import webdriver
link = "http://suninjuly.github.io/find_link_text_redirect13.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input[name='first_name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city[name='firstname']")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
