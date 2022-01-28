from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 
import engine as e

username={
	"Abhijeet":"ringeshubhangi21@gmail.com"
}
password={
	"Abhijeet":"shubha2108"
}
  
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/login/')
print ("Opened facebook")
sleep(1)


name= e.face_webcam()
if name=="Abhijeet":
	usr=username[name]
	pwd=password[name]

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)
  
password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print ("Password entered")
  
login_box = driver.find_element_by_id('loginbutton')
login_box.click()