from selenium import webdriver
import time 

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")

input1 = browser.find_element_by_tag_name("input").send_keys("Ivan")
input2 = browser.find_element_by_name("last_name").send_keys("Petrov")
input3 = browser.find_element_by_class_name("form-control.city").send_keys("Smolensk")
input4 = browser.find_element_by_id("country").send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn").click()


    # успеваем скопировать код за 5 секунд
time.sleep(5)
    # закрываем браузер после всех манипуляций
browser.quit()

# не забываем оставить пустую строку в конце файла
