from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

#расчет и возврат значения функции
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

#вводим получившиеся значение
input1 = browser.find_element_by_id("answer").send_keys(y)

#ставим галочку мы робот
option2 = browser.find_element_by_id("robotCheckbox").click()

#ставим галочку что роботы рулят

option3 = browser.find_element_by_id("robotsRule").click()

# Отправляем заполненную форму
button = browser.find_element_by_class_name("btn.btn-default").click()

time.sleep(5)

browser.quit()