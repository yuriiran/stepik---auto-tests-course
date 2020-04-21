from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

#расчет и возврат значения функции
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

#вводим получившиеся значение

browser.execute_script("window.scrollBy(0, 100);")

input = browser.find_element_by_id("answer")
#browser.execute_script("return arguments[0].scrollIntoView({block: '100'});", input)
input.send_keys(y)

#ставим галочку мы робот
option2 = browser.find_element_by_id("robotCheckbox")
#browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", option2)
option2.click()
#ставим галочку что роботы рулят

option3 = browser.find_element_by_id("robotsRule")
#browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", option3)
option3.click()

# Отправляем заполненную форму
button = browser.find_element_by_class_name("btn.btn-primary")
#browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", button)
button.click()

time.sleep(10)

browser.quit()