import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


class AlertAccept:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

# push button
	send_button1 = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
	send_button1.click()

# swicth window
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

	# находим значение x
	num1 = browser.find_element(By.XPATH, '//*[@id="input_value"]')
	num1_Num = int(num1.text)

# высчитываем результат для задания
	test_result = str(math.log(abs(12 * math.sin(int(num1_Num)))))

# вводим ответ
	element1 = browser.find_element_by_css_selector('#answer')
	element1.send_keys(test_result)

# нажимаем кнопку отправить
	option1 = browser.find_element_by_css_selector("[type='submit']")
	option1.click()

	time.sleep(5)
	browser.quit()
