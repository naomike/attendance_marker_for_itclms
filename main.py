import os
import datetime
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


load_dotenv()

# calculate class period
now_dt = datetime.datetime.now()
dow = now_dt.weekday()
if dow == 6:
    raise Exception("Today is Sunday. Take some rest!")

present_time_str = str(now_dt.hour).zfill(2) + str(now_dt.minute).zfill(2)
class_periods = ['0825', '1015', '1210', '1445', '1640', '1835']
for i in range(len(class_periods) - 1):
    if class_periods[i] <= present_time_str[i+1]:
        period = i + 1
        break
else:
    raise Exception('It is outside of school hours. Did you miss any class?')


print("Enter a passcode for attendance: ")
passcode = input()

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://itc-lms.ecc.u-tokyo.ac.jp/login")

# login
driver.find_element_by_xpath('//a[@href="/saml/login?disco=true"]').click()
user_name_box = driver.find_element_by_name("UserName")
user_name_box.send_keys(os.environ['USER_NAME'])
password_box = driver.find_element_by_name("Password")
password_box.send_keys(os.environ['PASSWORD'])
password_box.send_keys(Keys.ENTER)

# find the lecture
lecture_xpath = "/html/body/div[1]/div[2]/div[1]/div[2]/form[1]/div[2]/div/div[{}]/div[{}]/div/div[1]".format(
    str(period + 1), str(dow + 2)
)
try:
    driver.find_element_by_xpath(lecture_xpath).click()
except NoSuchElementException:
    raise Exception('You do not have any class now')


# send passcode
try:
    time.sleep(3)
    password_box_xpath = "/html/body/div[1]/div[2]/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div/a"
    driver.find_element_by_xpath(password_box_xpath).click()

    time.sleep(3)

    text = driver.find_element_by_name("oneTimePass")
    text.send_keys(passcode)
    send_password_xpath = "/html/body/div[3]/div[3]/div/button[2]"
    driver.find_element_by_xpath(send_password_xpath).click()
except NoSuchElementException:
    raise Exception('Could not find a passcode box. You may not need to mark attendace for this class')
