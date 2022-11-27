import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup

import requests

import time
import random

from common.Log_info import LogInfo


driver = webdriver.Chrome()

class ScrapeSales(LogInfo):
    
    
    def __init__(self, driver):
        self.url = r'https://owner.yogiyo.co.kr/owner/orders/'


    def select_store(self, driver, store_index):
        ran_num = round(random.random())
        driver.page_source
        name_list = driver.find_elements(By.CLASS_NAME, '.name')
        this_name = self.getStore[store_index]

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="selectedStore"]/div[1]/button')
        )).click()
                        
        for name in name_list:
            if ('프랭크' in name) and (this_name[:2] in name):
                driver.find_elements(By.CLASS_NAME, '.name')[name].click()
            else:
                print('no store')
            
        

        
        
        
        
        pass

    def select_date(self, driver, store_index):
        pass

    def get_sales(self, dirver, store_index):
        pass







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