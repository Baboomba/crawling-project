import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup

import requests

import time


# performing web driver
option = webdriver.ChromeOptions()
option.add_argument('headless')

url = 'https://owner.yogiyo.co.kr/owner/'
driver = webdriver.Chrome(executable_path=r'C:\Users\SEC\chromedriver')
# driver = webdriver.Chrome(executable_path='chromedriver', chrome_options = option)
driver.get(url = url)


# parsing the main pages
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
time.sleep(1.5)


# trying log in
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[1]/a[1]/button').click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/form/div[1]/div/input').click()
time.sleep(1)
webdriver.ActionChains(driver).send_keys('jiyun88').key_down(Keys.TAB).key_up(Keys.TAB).send_keys('jiyun1988^^').perform()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/form/button').click()
time.sleep(1.5)

# renewing html
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


# selecting the frankburger
driver.find_element(By.XPATH, '//*[@id="selectedStore"]/div[1]/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="vendorList"]/li[2]/ul/li/p').click()


# selecting the date
driver.find_element(By.XPATH, '//*[@id="start_date"]').click()
# driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]/span').click() 달수 넘기기
# driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[4]/a').click()
driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[4]/a').click()
driver.find_element(By.XPATH, '//*[@id="end_date"]').click()
driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[5]/a').click()
#driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[4]/a').click()
driver.find_element(By.XPATH, '//*[@id="orders-filters-form"]/div[2]/button').click()


# renewing html
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


# getting the information
quantity = soup.select_one('#main > div:nth-child(3) > table > tbody > tr > td:nth-child(1) > div > strong').text
sales = soup.select_one('#main > div:nth-child(3) > table > tbody > tr > td:nth-child(2) > div > strong').text
tips_all = soup.find_all('tr')
tips_last = list(tips_all[-1])
tips = tips_last[5].text


# transforming string into integer
quantity = quantity.replace("건", "")
quantity = quantity.replace(",", "")
sales = sales.replace("원", "")
sales = sales.replace(",", "")
tips = tips.replace(",", "")
quantity = int(quantity)
sales = int(sales)
tips = int(tips)


# creating dataframe
empty = pd.DataFrame(index = range(0, ), columns = ["매출", "건수", "배달팁"])
values = [sales, quantity, tips]
empty.loc["가맹점"] = values


# saving data
empty.to_excel(r'C:\Users\SEC\Coding\VScode\crawling\yogiyo\sales.xlsx')


# closing code
driver.close

print("complete")