from selenium import webdriver
import time

#sigwan = webdriver.Chrome('C:\\Users\\rhtjd\\AppData\\Local\\Programs\\Python\\chromedriver.exe')
#url = 'http://comci.kr/st/'
#sigwan.get(url)
#time.sleep(3)
#test = sigwan.find_element_by_xpath("/html/frameset")

driver = webdriver.Chrome('C:\\Users\\rhtjd\\AppData\\Local\\Programs\\Python\\chromedriver.exe')
url = 'https://hoc.ebssw.kr/sso/loginView.do?loginType=onlineClass'
driver.get(url)
find = driver.find_element_by_xpath("//input[@id='j_username']")
find.clear()  # 글자 지움
find.send_keys("rhtjdsh35") # 글자 입력
find = driver.find_element_by_xpath("//input[@id='j_password']")
find.clear()  # 글자 지움
find.send_keys("zxc6430771") # 글자 입력
time.sleep(2)
search = driver.find_element_by_xpath("//button[@type='button']")
search.click()
time.sleep(5)
url = 'https://hoc10.ebssw.kr/cbejcjeilhs02/hmpg/hmpgAlctcrListView.do?menuSn=315398'
driver.get(url)
