from selenium import webdriver
import time
import math

link=("http://suninjuly.github.io/selects2.html")

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("num1")
x = x_element.text
y_element = browser.find_element_by_id("num2")
y = y_element.text

def calc():
    z = str(int(x) + int(y))
    return z
z = calc()

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(z)

# Отправляем заполненную форму
button = browser.find_element_by_class_name("btn.btn-default").click()

time.sleep(10)
browser.quit()