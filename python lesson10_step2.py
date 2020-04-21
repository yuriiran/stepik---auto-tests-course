from selenium import webdriver
import time
import math
import pyperclip

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
#нажимвем кнопку
    button = browser.find_element_by_class_name("trollface.btn.btn-primary").click()

#переход на новое окно браузера
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

#решаем задачу
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

#вводим ответ 
    input1 = browser.find_element_by_id("answer").send_keys(y)

# Отправляем заполненную форму
    button = browser.find_element_by_class_name("btn.btn-primary").click()

#копируем число и вставляем в ответ 
# спасибо за данную часть VitaliyYa

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)


finally:
    time.sleep(10)
    browser.quit()

