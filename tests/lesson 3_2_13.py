from selenium import webdriver
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_page_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".first_block > .first_class > input.first")
        input1.send_keys("Artem")
        input2 = browser.find_element_by_css_selector(".first_block > .second_class > input.second")
        input2.send_keys("Sviridov")
        input3 = browser.find_element_by_css_selector(".first_block > .third_class > input.third")
        input3.send_keys("mail@mail.ru")
        ...

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        expected_welcome_text = 'Congratulations! You have successfully registered!'
        self.assertEqual(welcome_text, expected_welcome_text, 'okay')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_page_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(".first_block > .first_class > input.first")
        input1.send_keys("Artem")
        input2 = browser.find_element_by_css_selector(".first_block > .second_class > input.second")
        input2.send_keys("Sviridov")
        input3 = browser.find_element_by_css_selector(".first_block > .third_class > input.third")
        input3.send_keys("mail@mail.ru")
        ...

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        expected_welcome_text = 'Congratulations! You have successfully registered!'
        self.assertEqual(welcome_text, expected_welcome_text, 'okay')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
