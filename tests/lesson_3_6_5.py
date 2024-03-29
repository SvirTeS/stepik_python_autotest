import pytest
import time
import math
import login
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('urls', ['https://stepik.org/lesson/236895/step/1',
                                  'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1',
                                  'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1',
                                  'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1',
                                  'https://stepik.org/lesson/236905/step/1'])
class TestStepik:
    def test_login_stepik(self, browser, urls):
        link = urls
        browser.get(link)
        browser.find_element(By.XPATH, "//header[@id='main-header']//*[contains(@class, 'navbar__auth_login')]").click()
        browser.find_element(By.XPATH, "//form[@id='login_form']//*[contains(@name, 'login')]").send_keys(login.email)
        browser.find_element(By.XPATH, "//form[@id='login_form']//*[contains(@name, 'password')]").send_keys(login.password)
        browser.find_element(By.XPATH, "//form[@id='login_form']//*[contains(@type, 'submit')]").click()
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, "//*[contains(@class, 'string-quiz__textarea')]").send_keys(self.answer())
        time.sleep(1)
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, "//*[contains(@class, 'submit-submission')]").click()
        time.sleep(3)
        browser.implicitly_wait(5)
        correctly = browser.find_element(By.XPATH, "//*[@class='smart-hints__hint']")
        assert correctly == 'Correct!'

    def answer(self):
        return str(math.log(int(time.time())))

