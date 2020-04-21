from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    from sendToStepik import sendToStepik
    # в переменную task_link вставить адрес страницы с заданием
    task_link = 'https://stepik.org/lesson/184253/step/4?unit=158843'

#нажимвем кнопку
    button = browser.find_element_by_class_name("btn.btn-primary").click()

#нажаимаем согласие
    alert = browser.switch_to.alert
    alert.accept()

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

#корируем значение из окна

# Копирование числа из алерта
    #alert = browser.switch_to.alert
    #alert_text = alert.text
    #alert.accept()
    #answer = alert_text.split(': ')[-1]


# Отправка решения на Stepik:
    #sendToStepik(task_link, answer)

#копируем число и вставляем в ответ
finally:
    time.sleep(10)
    browser.quit()
