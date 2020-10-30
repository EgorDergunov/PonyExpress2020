from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import pathes

   
def pony_driver_init(driver_path):
   if pathes.browser == 'Firefox':
      driver = webdriver.Firefox(executable_path=driver_path)
   if pathes.browser == 'Chrome':
      driver = webdriver.Chrome(executable_path=driver_path)
   address = pathes.pegas_url
   driver.get(address)
   
   try:
       title = WebDriverWait(driver,30).until(EC.title_is('Пегас'))
       print('Страницу открыли')
   except:
       print('Page not opened')
       driver.close()
   return driver

def pegas_open():
   try:
       driver_path = pathes.driverpath
       driver = pony_driver_init(driver_path)
       element_login = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME, 'login')))
       element_password = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME, 'password')))
       enter_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'css-1hnkt5t')))
       print('Окно логина нашли')
   except:
       print ('Login not found')
       driver.close()
       

   correct_login = pathes.login
   correct_password = pathes.password

   element_login.send_keys(correct_login)
   element_password.send_keys(correct_password)
   enter_button.click()
   try:
       flag = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'bp3-button-text')))
       print('Вход выполнен')
   except:
       print ('Can not enter')
       driver.close()
   return driver

def input_object_number(driver,obj_number):
   try:
       object_number = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[3]/div[2]/div/div/div[3]/form/input')))
       object_number.send_keys(obj_number)
       object_number.send_keys('\n')
       print('Номер объекта введён')
   except:
       print ('Can not send object number')
       driver.close()

def case_10(driver):
   import test13
   test13.case_13(driver)

   input_object_number(driver,'99-9999-9999/999')
   
   if __name__ == '__main__':
      driver.close()
   
   
   

if __name__ == '__main__':
   driver = pegas_open()
   case_10(driver)

