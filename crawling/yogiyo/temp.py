from platform import java_ver
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import sys

from common.Log_info import LogInfo

import pandas as pd

import requests

from bs4 import BeautifulSoup


import time

url_1 = r'https://ceo.yogiyo.co.kr/login?by_dowant=1'
url_2 = r'https://owner.yogiyo.co.kr/owner/login/'
url_3 = r'https://owner.yogiyo.co.kr/owner/orders/'


options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging']) 

driver = webdriver.Chrome(executable_path=r'C:\Users\SEC\chromedriver')


# variable of log_in
wb = pd.read_excel(r'C:\Users\SEC\Coding\VScode\crawling\store_list.xls')
log = log_info()
shape_df = wb.shape[0]


# extracting data of Yogiyo

def get_y_data():
    




# trying log in
for i in range(0, shape_df):
    try:
        driver.get(url = url_1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(1.5)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/form/div[1]/div/input').click()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(log.get_ygyid(i)).key_down(Keys.TAB).key_up(Keys.TAB).send_keys(log.get_ygypw(i)).perform()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/form/button').click()
        time.sleep(1.5)
    
        if driver.current_url == url_3:
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            time.sleep(1.5)
            driver.find_element(By.XPATH, '//*[@id="selectedStore"]/div[1]/span[2]').click()
            driver.find_element(By.XPATH, '//*[@id="vendorList"]/li[2]/ul/li/p').click()
    
        else:
            driver.get(url = url_2)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            time.sleep(1.5)
            driver.find_element(By.XPATH, '//*[@id="username"]').click()
            time.sleep(1)
            webdriver.ActionChains(driver).send_keys(log.get_ygyid(i)).key_down(Keys.TAB).key_up(Keys.TAB).send_keys(log.get_ygypw(i)).perform()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/form/button').click()
            time.sleep(1.5)
    

    except:
        print('no yogiyo id')
        
        
        
        

'''
class log_try:
    url_1 = r'https://ceo.yogiyo.co.kr/login?by_dowant=1'
    url_2 = r'https://owner.yogiyo.co.kr/owner/login/'
    url_3 = r'https://owner.yogiyo.co.kr/owner/orders/'
    driver = webdriver.Chrome(executable_path=r'C:\Users\SEC\chromedriver')
    def ygy_try(self):
        try:
            for i in range(0, shape_df):
                driver.get(url = url_1)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                time.sleep(1.5)
                driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/form/div[1]/div/input').click()
                time.sleep(1)
                webdriver.ActionChains(driver).send_keys(log.get_ygyid(i)).key_down(Keys.TAB).key_up(Keys.TAB).send_keys(log.get_ygypw(i)).perform()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/form/button').click()
                time.sleep(1.5)
    
                if driver.current_url == url_3:
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    time.sleep(1.5)
                    driver.find_element(By.XPATH, '//*[@id="selectedStore"]/div[1]/span[2]').click()
                    driver.find_element(By.XPATH, '//*[@id="vendorList"]/li[2]/ul/li/p').click()
                    BeautifulSoup.find_all('vendorList', )
    
                else:
                    driver.get(url = url_2)
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    time.sleep(1.5)
                    driver.find_element(By.XPATH, '//*[@id="username"]').click()
                    time.sleep(1)
                    webdriver.ActionChains(driver).send_keys(log.get_ygyid(i)).key_down(Keys.TAB).key_up(Keys.TAB).send_keys(log.get_ygypw(i)).perform()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/form/button').click()
                    time.sleep(1.5)
                
        except:
            print('no yogiyo id')
# to use 'find_all' function // self variable needed in first
htmlhtml = driver.page_source
soupsoup = BeautifulSoup(htmlhtml, 'html.parser')
# c_num = driver.find_element(By.CLASS_NAME, 'company-number')
rdval = BeautifulSoup.find_all(soupsoup, 'li', attrs={'class' : 'vendor-group'})'''