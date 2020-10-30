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

def case_13(driver):
   
   try:
       menu_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[1]/div/div/span/span/button')))
       menu_button.click()
       print('Кнопку меню нажали')
   except:
       print ('Can not find menu button')
       driver.close()
   try:
       proizv_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/span')))
       proizv_button.click()
       print('Кнопку Производство нажали')
   except:
       print ('Can not find "Производство" button')
       driver.close()
   try:
       reg_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/span')))
       reg_button.click()
       print('Кнопку Регистрация событий нажали')
   except:
       print ('Can not find "Регистрация событий" button')
       driver.close()
   try:
       case_79_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[4]/a')))
       case_79_button.click()
       print('Кнопку "79 - Включен в консолидацию" нажали')
   except:
       print ('Can not find "79 - Включен в консолидацию" button')
       driver.close()
  
   
   time.sleep(10)
   
   print (driver.window_handles)
   driver.switch_to.window(driver.window_handles[1])
   
   try:
       choose_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/button')))
       choose_button.click()
       print('Кнопку Выбрать нажали')
   except:
       print ('Can not find "Выбрать" button')
       driver.close()
   try:
       search = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-input"]')))
       search.send_keys('1202')
       print('Номер точки назначения ввели')
   except:
       print ('Can not send keys 1202')
       driver.close()
   time.sleep(2)
   try:
       checkbox = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/label')))
       checkbox.click()
       print('Галку нажали')
   except:
       print ('Can not choose destination')
       driver.close()
   try:
       add_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[1]')))
       add_button.click()
       print('Кпопку Добавить нажали')
   except:
       print ('Can not find Добавить button')
       driver.close()

   
   try:
       continue_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button')))
       continue_button.click()
       print('Кпопку Далее нажали')
   except:
       print ('Can not find Далее button')
       driver.close()

   try:
       check_number = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/div')))
       check_number.text == '1202'
       print('Номер внесли')
   except:
       print ('Number is incorrect')
       driver.close()
       
   if __name__ == '__main__':
      driver.close()
   
   
   

if __name__ == '__main__':
   driver = pegas_open()
   case_10(driver)

