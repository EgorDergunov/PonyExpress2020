from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def case_0():
   driver_path = r'C:\Users\Дергунов Денис\Desktop\geckodriver.exe'
   driver = webdriver.Firefox(executable_path=driver_path)

   driver.get("http://pegasus-edu.pegasus.ponyex.local/")
   assert "Пегас" == driver.title

   element_login = driver.find_element_by_name("login")
   element_password = driver.find_element_by_name("password")
   enter_button = driver.find_element_by_class_name("css-1hnkt5t")

   time.sleep(10)
   correct_login = 'ext.mgu_education'
   correct_password = 'rg#P5hZm4F'

   element_login.send_keys(correct_login)
   element_password.send_keys(correct_password)


   enter_button.click()
   time.sleep(5)

   pegas = driver.find_element_by_class_name("bp3-button-text")
   
   if pegas.text == 'ПЕГАС 2.0':
      return 'Yes'
   else: return 'No'
   driver.close()



   
def pony_driver_init(driver_path):
   
   driver = webdriver.Firefox(executable_path=driver_path)

   driver.get("http://pegasus-edu.pegasus.ponyex.local/")

   try:
       title = WebDriverWait(driver,30).until(EC.title_is('Пегас'))
   except:
       print('Page not opened')
       driver.close()
   return driver


def case_1():
   try:
       driver_path = r'C:\Users\Дергунов Денис\Desktop\geckodriver.exe'
       driver = pony_driver_init(driver_path)
       element_login = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, 'login')))
       element_password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME, 'password')))
       enter_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-1hnkt5t')))
   except:
       print ('Login not found')
       driver.close()
   #return driver
       

   correct_login = 'ext.mgu_education'
   correct_password = 'rg#P5hZm4F'

   element_login.send_keys(correct_login)
   element_password.send_keys(correct_password)
   enter_button.click()
   try:
       flag = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, 'bp3-button-text')))
   except:
       print ('Can not enter')
       driver.close()
   time.sleep(10)
   driver.close()

print (case_1())
