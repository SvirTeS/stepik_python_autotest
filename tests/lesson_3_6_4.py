import pytest

import login
import time
from selenium.webdriver.common.by import By


class TestStepik():
    def test_login_stepik(self, browser):
        browser.get('https://stepik.org/lesson/236895/step/1')
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, "//header[@id='main-header']//*[contains(@class, 'navbar__auth_login')]")
        input1 = browser.find_element(By.XPATH, '//*[@id="id_login_email"]')
        input1.send_keys(login.email)
        input2 = browser.find_element(By.XPATH, '//*[@id="id_login_password"]')
        input2.send_keys(login.password)
        login_button = browser.find_element(By.XPATH, '//*[@id="login_form"]/button')
        login_button.click()
