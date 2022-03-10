""" from lib2to3.pgen2.driver import Driver
import time
from selenium import webdriver
from multiprocessing.connection import Client
import time
from ppadb.client import Client as AdbClient

client =AdbClient(host="127.0.0.1",port=5037)
devices=client.devices()
time2=time.sleep(2)
if len(devices)==0:
    print ("no device")
    quit()
device=devices[0]
print (f"connected{device}")

id="234345664046"
password="60832"
url="https://m.kuku.lu"
mails=["ofbuddog","brafit653","cupjamtee","budhum735","mudplyice","msrug805"]
passwords=["ofbuddog","brafit653","cupjamtee","budhum735","mudplyice","msrug805"]
usernames=["ofbuddog","brafit653","cupjamtee","budhum735","mudplyice","msrug805"]
names=["akın","ayşe","tarık","aslı","ali","gunay"]
surnames=["ter","veli","akıl","remzi","kapı","kel"]
domain="@exdonuts.com"
for item in range(1):
    driver = webdriver.Chrome()
    driver.get(url)
    chaccbtn=driver.find_element_by_id("link_loginform")
    inputId=driver.find_element_by_id("user_number")
    inputPas=driver.find_element_by_id("user_password")
    loginBtn=driver.find_element_by_xpath("/html/body/div[1]/div[15]/div/div/form/div[3]/a")
    createBtn=driver.find_element_by_id("link_addMailAddrByAuto")
 
    chaccbtn.click()
    time.sleep(2)
    inputId.send_keys(id)
    time.sleep(2)
    inputPas.send_keys(password)
    time.sleep(2)
    loginBtn.click()

    time.sleep(1)
    a=driver.find_element_by_id("link_addMailAddrByAuto")
    a.click()

    text=driver.find_element("b").get_attribute("innerHTML")
    print(text)
    time.sleep(5)
    b=driver.find_element_by_id("link_newaddr_close")
    b.click()
 
    time.sleep(1)
    #airplane mode keyevent 
    device.shell("am start -a android.settings.AIRPLANE_MODE_SETTINGS ")
    time.sleep(2)
    driver.get(url)
    #tap airplane mode on off
    device.shell('input touchscreen tap 239 244')
    time.sleep(5)
    device.shell('input touchscreen tap 239 244')
    time.sleep(5)
    device.shell('input keyevent 3') 
    """