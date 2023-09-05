import pytest

import login
from selenium.webdriver.common.by import By


class TestStepik:
    def test_login_stepik(self, browser):
        browser.get('https://stepik.org/lesson/236895/step/1')
        browser.find_element(By.XPATH, "//header[@id='main-header']//*[contains(@class, 'navbar__auth_login')]").click()
        browser.find_element(By.XPATH, "//form[@id='login_form']//*[contains(@name, 'login')]").send_keys(login.email)
        browser.find_element(By.XPATH, "//form[@id='login_form']//*[contains(@name, 'password')]").send_keys(login.password)
        browser.find_element(By.XPATH, "//form[@id='login_form']//*[contains(@type, 'submit')]").click()


