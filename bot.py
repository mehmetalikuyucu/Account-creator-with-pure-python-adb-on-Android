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
#read files
mail=open("mail.txt","r")
name=open("name.txt","r")
surname=open("surname.txt","r")
username=open("username.txt","r")
password=open("password.txt","r")
passwords=password.readlines()
surnames=surname.readlines()
mails=mail.readlines()
names=name.readlines()
usernames=username.readlines()



for item in range(50):
    print(item)
    #tap duckduckgo
    time.sleep(1)
    device.shell('input touchscreen tap 495 545')
    time.sleep(3)

    #input text
    device.shell('input  text "google.com"')
    time.sleep(2)

    #keyevent enter
    device.shell('input keyevent 66')
    time.sleep(9)

    #tap account logo
    device.shell('input touchscreen tap 514 329')
    time.sleep(3)

    #tap no account text
    device.shell('input touchscreen tap 481 915')
    time.sleep(3)

    #tap mail
    device.shell('input touchscreen tap 255 450')
    time.sleep(1)
    device.shell('input touchscreen tap 255 450')
    device.shell(f'input  text "{mails[item]}"')
    time.sleep(3)
    #tap name
    device.shell('input touchscreen tap 190 565')
    time.sleep(1)
    device.shell('input touchscreen tap 190 565')
    time.sleep(1)
    device.shell(f'input  text "{names[item]}"')
    time.sleep(3)

    #tap surname
    device.shell('input touchscreen tap 626 565')
    time.sleep(1)
    device.shell('input touchscreen tap 626 565')
    device.shell(f'input  text "{surnames[item]}"')
    time.sleep(3)

    #tap pass
    device.shell('input touchscreen tap 290 705')
    time.sleep(2)
    device.shell(f'input  text "{passwords[item]}"')
    time.sleep(2)

    #tap passcheck
    device.shell('input touchscreen tap 570 705')
    time.sleep(2)
    device.shell(f'input  text "{passwords[item]}"')
    time.sleep(2)

    #tap username
    device.shell('input touchscreen tap 312 811')
    time.sleep(2)
    device.shell(f'input  text "{usernames[item]}"')
    time.sleep(1)
    device.shell(f'input text "{usernames[item+5]}"')
    time.sleep(1)
    device.shell('input touchscreen swipe 382 742 382 218')
    time.sleep(1)
    #swipe for above

    #tap gender
    device.shell('input touchscreen tap 220 336')
    time.sleep(1)
    device.shell('input touchscreen tap 245 720')
    time.sleep(1)

    #tap day
    device.shell('input touchscreen tap 255 902')
    time.sleep(1)
    device.shell('input touchscreen tap 310 682')
    time.sleep(1)

    #tap month
    device.shell('input touchscreen tap 437 902')
    time.sleep(1)
    device.shell('input touchscreen tap 310 682')
    time.sleep(1)

    #tap year
    device.shell('input touchscreen tap 680 902')
    time.sleep(1)
    device.shell('input touchscreen swipe 382 1000 382 100')
    time.sleep(1)
    device.shell('input touchscreen swipe 382 1000 382 100')
    time.sleep(1)
    device.shell('input touchscreen swipe 382 1000 382 100')
    time.sleep(1)
    device.shell('input touchscreen swipe 382 1000 382 100')
    time.sleep(1)
    device.shell('input touchscreen tap 245 920')
    time.sleep(1)

    #tap checkbox
    device.shell('input touchscreen tap 75 1016')
    time.sleep(1)

    #tap sendbutton
    device.shell('input touchscreen tap 465 1153')
    time.sleep(2)

    #back
    device.shell('input keyevent 4')
    time.sleep(1)

    #tap bürst
    device.shell('input touchscreen tap 522 117')
    time.sleep(2)

    #tap ok
    device.shell('input touchscreen tap 500 1310')
    time.sleep(2)

    #tap home
    device.shell('input keyevent 3')
    time.sleep(1)

    #airplane mode keyevent
    device.shell("am start -a android.settings.AIRPLANE_MODE_SETTINGS ")
    time.sleep(2)

    #tap airplane mode on off
    device.shell('input touchscreen tap 239 244')
    time.sleep(5)
    device.shell('input touchscreen tap 239 244')
    time.sleep(5)
    device.shell('input keyevent 3')




