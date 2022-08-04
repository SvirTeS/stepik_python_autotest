import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


class ExecuteScript:
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

# находим значение x
	num1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
	num1_Num = int(num1.text)


# высчитываем результат для задания
	test_result = str(math.log(abs(12*math.sin(int(num1_Num)))))


# вводим ответ
	element1 = browser.find_element_by_css_selector('#answer')
	element1.send_keys(test_result)


# нажимаем кнопку отправить
	option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
	option1.click()
	option2 = browser.find_element_by_css_selector("#robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
	option2.click()
	option3 = browser.find_element_by_css_selector("[type='submit']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", option3)
	option3.click()

	time.sleep(5)
	browser.quit()
