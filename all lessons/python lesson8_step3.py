from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

#заполняем обязательные поля
input1 = browser.find_element_by_name("firstname").send_keys("Yura")
input2 = browser.find_element_by_name("lastname").send_keys("KL")
input3 = browser.find_element_by_name("email").send_keys("email")

#загружаем файл
import os 
button = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
button.send_keys(file_path)

# Отправляем заполненную форму
button = browser.find_element_by_class_name("btn.btn-primary").click()

time.sleep(10)
browser.quit()
