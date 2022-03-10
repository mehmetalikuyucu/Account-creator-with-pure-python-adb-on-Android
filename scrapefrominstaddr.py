import time
from selenium import webdriver
from bs4 import BeautifulSoup
id="894266473000"
password="109190"
url="https://m.kuku.lu"
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
time.sleep(5)
"""
for item in range(50):
    time.sleep(1)
    a=driver.find_element_by_id("link_addMailAddrByAuto")
    a.click()
    time.sleep(5)
    b=driver.find_element_by_id("link_newaddr_close")
    b.click()
"""
document=BeautifulSoup(driver.page_source,"html.parser")
mailList=document.findAll(class_="vcenter")

mailtxt=open("mail.txt","w")
for item in mailList:
    mailtxt.write(item.getText())

driver.quit()



