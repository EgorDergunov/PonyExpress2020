from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = r'C:\Users\Дергунов Денис\Desktop\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)

driver.get("http://pegasus-edu.pegasus.ponyex.local/")
assert "Пегас" == driver.title

element_login = driver.find_element_by_name("login")
element_password = driver.find_element_by_name("password")
enter_button = driver.find_element_by_class_name("css-1hnkt5t")

element_login.send_keys("login")
element_password.send_keys("password")
enter_button.click()

elem = driver.find_element_by_xpath('/html/body/div[1]/section/form/p')
elem.text

element_login.clear()
element_password.clear()

correct_login = 'ext.mgu_education'
correct_password = 'rg#P5hZm4F'

element_login.send_keys(correct_login)
element_password.send_keys(correct_password)

enter_button.click()

driver.close()
