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
       print('Страницу открыли')
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
       print('Окно логина нашли')
   except:
       print ('Login not found')
       driver.close()
   correct_login = 'ext.mgu_education'
   correct_password = 'rg#P5hZm4F'

   element_login.send_keys(correct_login)
   element_password.send_keys(correct_password)
   enter_button.click()
   try:
       flag = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, 'bp3-button-text')))
       print('Вход выполнен')
   except:
       print ('Can not enter')
       driver.close()
   time.sleep(10)
   driver.close()


def case_6():
   try:
       driver_path = r'C:\Users\Дергунов Денис\Desktop\geckodriver.exe'
       driver = pony_driver_init(driver_path)
       element_login = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME, 'login')))
       element_password = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME, 'password')))
       enter_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'css-1hnkt5t')))
       print('Окно логина нашли')
   except:
       print ('Login not found')
       driver.close()
       

   correct_login = 'ext.mgu_education'
   correct_password = 'rg#P5hZm4F'

   element_login.send_keys(correct_login)
   element_password.send_keys(correct_password)
   enter_button.click()
   try:
       flag = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'bp3-button-text')))
       print('Вход выполнен')
   except:
       print ('Can not enter')
       driver.close()

   #new
   try:
       menu_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'bp3-intent-success')))
       menu_button.click()
       print('Кнопку меню нажали')
   except:
       print ('Can not find menu button')
       driver.close()
   try:
       servis_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[7]')))
       servis_button.click()
       print('Кнопку Сервис нажали')
   except:
       print ('Can not find servis button')
       driver.close()
   try:
       upravlenie_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span')))
       upravlenie_button.click()
       print('Кнопку Управление разрешениями нажали')
   except:
       print ('Can not find upravlenie razresheniyami button')
       driver.close()
   try:
       groups_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/ul/li[7]/span/div/div/div/div/ul/li[1]/span/div/div/div/div/ul/li[1]')))
       groups_button.click()
       print('Кнопку Группы пользователей нажали')
   except:
       print ('Can not find groups button')
       driver.close()
   try:
       flag1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'css-95g4uk')))
       print('Страницу Редактирование групп открыли')
   except:
       print ('Can not open the page with groups')
       driver.close()
   try:
       create_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/section[2]/section/section/div/div/div[1]/div[1]/button[1]')))
       create_button.click()
       print('Кнопку Создать новую нажали')
   except:
       print ('Can not find the button to create a new group')
       driver.close()
   try:
       element_name = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[1]/div/div/input')))
       save_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/form/div[2]/button[1]')))
       print('Название группы введено')
   except:
       print ('No place to write the name of the group')
       driver.close()
   group_name = 'Group 33'
   element_name.send_keys(group_name)
   save_button.click()

       
      
   time.sleep(10)
   #driver.close()
   
print (case_6())
