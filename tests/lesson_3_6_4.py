import pytest

import login
from selenium.webdriver.common.by import By


class TestStepik():
    def test_login_stepik(self, browser):
        browser.get('https://stepik.org/lesson/236895/step/1')
        browser.implicitly_wait(15)
        browser.find_element(By.XPATH, "//header[@id='main-header']//*[contains(@class, 'navbar__auth_login')]").click()
        input1 = browser.find_element(By.XPATH, "//form[@id='login_form']//*[contains(@name, 'login')]")
        input1.send_keys(login.email)
        input2 = browser.find_element(By.XPATH, "//form[@id='login_form']//*[contains(@name, 'password')]")
        input2.send_keys(login.password)
        login_button = browser.find_element(By.XPATH, "//form[@id='login_form']//*[contains(@type, 'submit')]")
        login_button.click()
