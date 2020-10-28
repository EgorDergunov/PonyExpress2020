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

def case_8(): 
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
       case_71_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[1]/span/div/div/div/div/ul/li[1]/span/div/div[2]/div/div/ul/li[1]/a/div')))
       case_71_button.click()
       print('Кнопку "71 - Прибыл на склад без сортировки" нажали')
   except:
       print ('Can not find "71 - Прибыл на склад без сортировки" button')
       driver.close()
  
   #print (driver.window_handles)
   
   time.sleep(15)
   driver.switch_to.window('43')

   try:
       vvod_dannih = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//html/body/div[3]/div/div[2]/div')))  
       print('Окно "Ввод данных о блоке" нашли')
   except:
       print ('Can not find "Ввод данных о блоке"')
       driver.close()
   try:
       cont_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div[1]/button[2]')))
       cont_button.click()
       print('Кнопку "Продолжить без курьера" нажали')
   except:
       print ('Can not find "Продолжить без курьера" button')
       driver.close()
   driver.close()


if __name__ == '__main__':
    driver = pegas_open()

case_8()

