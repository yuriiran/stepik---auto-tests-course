from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyperclip
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 15 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100") #устанавливаем откуда берем данные и на каком числе нажимаем кнопку
    )
button = browser.find_element_by_class_name("btn.btn-primary").click() #нажимаем кнопку

#решаем задачу
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

#вводим ответ 
input1 = browser.find_element_by_id("answer").send_keys(y)

# Отправляем заполненную форму
button = browser.find_element_by_id("solve").click() #поиск кнопки должен быть уникален

# Копирование числа из алерта в буфер обмена
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)


time.sleep(2)
browser.quit()