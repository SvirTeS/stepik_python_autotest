import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


class UploadFile:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

# вводим фио и почту
	first_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
	first_name.send_keys('user')
	last_name = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
	last_name.send_keys('testov')
	email = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
	email.send_keys('email@email.com')


# цепляем файл
	file = browser.find_element(By.XPATH, '//*[@id="file"]')
	current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
	file_path = os.path.join(current_dir, '../1.txt')  # добавляем к этому пути имя файла
	file.send_keys(file_path)


# нажимаем кнопку отправить
	send_button = browser.find_element(By.XPATH, "/html/body/div/form/button")
	send_button.click()

	time.sleep(5)
	browser.quit()
