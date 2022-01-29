from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
from recognition import get_utils,login_webcam
import sqlite3
from db_utils import connect,searchName,getCred,insertData
  
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/login/')
print ("Opened facebook")
sleep(1)

face_cascade,nn,labels = get_utils()
name = login_webcam(face_cascade,nn,labels)
name = name[0]

#search in database ... if not found make new entry
conn,cur = connect()
if searchName(cur,name):
	usr,pwd = getCred(cur,name)
else:
	print('Credentials not found..Add your credentials:')
	usr = input("Username: ")
	pwd = input("Password: ")
	insertData(conn,cur,name,usr,pwd)


username_box = driver.find_element(By.ID,'email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)

password_box = driver.find_element(By.ID,'pass')
password_box.send_keys(pwd)
print ("Password entered")

login_box = driver.find_element(By.ID,'loginbutton')
login_box.click()
print ("Done")
input('Press anything and enter to quit')
driver.quit()
print("Finished")