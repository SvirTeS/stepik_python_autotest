import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class SelectSum:
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)

# находим значения x и y для выполнения задания
	num1 = browser.find_element(By.XPATH, "//*[@id='num1']")
	num1_Num = int(num1.text)
	num2 = browser.find_element(By.XPATH, "//*[@id='num2']")
	num2_Num = int(num2.text)

# высчитываем результат для задания
	test_result = int(num1_Num) + int(num2_Num)

# выбираем ответ в списке
	browser.find_element(By.CLASS_NAME, "custom-select").click()
	browser.find_element(By.CSS_SELECTOR, f"[value='{test_result}']").click()

# нажимаем кнопку отправить
	send_button = browser.find_element(By.XPATH, "/html/body/div/form/button")
	send_button.click()

	time.sleep(5)
	browser.quit()
	