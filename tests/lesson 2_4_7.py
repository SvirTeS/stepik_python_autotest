from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


class Booking():

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока цена не снизится до 100
    book = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element(By.XPATH, '//*[@id="book"]')
    button.click()

# находим значение x
    num1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    num1_Num = int(num1.text)

# высчитываем результат для задания
    test_result = str(math.log(abs(12 * math.sin(int(num1_Num)))))

# вводим ответ
    element1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", element1)
    element1.send_keys(test_result)

# нажимаем кнопку отправить
    option1 = browser.find_element(By.XPATH, '//*[@id="solve"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    time.sleep(5)
    browser.quit()