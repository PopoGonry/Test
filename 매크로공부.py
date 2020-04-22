from selenium import webdriver
import time
import pyautogui
from datetime import datetime
import datetime

#sigwan = webdriver.Chrome('C:\\Users\\rhtjd\\AppData\\Local\\Programs\\Python\\chromedriver.exe')
#url = 'http://comci.kr/st/'
#sigwan.get(url)
#time.sleep(3)
#test = sigwan.find_element_by_xpath("/html/frameset")

#driver = webdriver.Chrome('C:\\Users\\rhtjd\\AppData\\Local\\Programs\\Python\\chromedriver.exe')
#url = 'https://hoc.ebssw.kr/sso/loginView.do?loginType=onlineClass'
#driver.get(url)
#find = driver.find_element_by_xpath("//input[@id='j_username']")
#find.clear()  # 글자 지움
#find.send_keys("rhtjdsh35") # 글자 입력
#find = driver.find_element_by_xpath("//input[@id='j_password']")
#find.clear()  # 글자 지움
#find.send_keys("zxc6430771") # 글자 입력
#time.sleep(2)
#search = driver.find_element_by_xpath("//button[@type='button']")
#search.click()
#time.sleep(5)
#url = 'https://hoc10.ebssw.kr/cbejcjeilhs02/hmpg/hmpgAlctcrListView.do?menuSn=315398'
#driver.get(url)

t = ['월', '화', '수', '목', '금', '토', '일']
r = datetime.datetime.today().weekday()
print(t[r], '의 시간표에 변경사항이 있으신가요?:')
Chan = input(str())
if(Chan == '아니요'):
    Gyo1 = '기존'
    Gyo2 = '기존'
    Gyo3 = '기존'
    Gyo4 = '기존'
    Gyo5 = '기존'
    Gyo6 = '기존'
    Gyo7 = '기존'
elif(Chan == '네'):
    print(t[r], '의 시간표를 입력해주세요.:')
    Gyo1 = input(str('1교시 : '))
    Gyo2 = input(str('2교시 : '))
    Gyo3 = input(str('3교시 : '))
    Gyo4 = input(str('4교시 : '))
    Gyo5 = input(str('5교시 : '))
    Gyo6 = input(str('6교시 : '))
    Gyo7 = input(str('7교시 : '))
else:
    print('"네 또는 "아니요" 만 입력해주세요.')

#시간표 인식 로직
#pyautogui.locateAllOnScreen("C:\\Users\\rhtjd\\Desktop\\Sigwan\\Fri.png")
#t = ['월', '화', '수', '목', '금', '토', '일']
#r = datetime.datetime.today().weekday()
#if(t[r] == '목'):
#    
#    print(s)