import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

import requests

from bs4 import BeautifulSoup

import sys
sys.path.append(r'C:\\Users\\SEC\\Coding\\VScode\\crawling')

from common.Log_info import LogInfo

import time

import openpyxl


option = webdriver.ChromeOptions()
option.add_argument('headless')


url_request = 'https://self.baemin.com/v1/settle/history/details?page=0&size=10&startDate=2022-10-01&endDate=2022-10-31'


# 
URL = r"https://ceo.baemin.com/web/login?returnUrl=https%3A%2F%2Fceo.baemin.com%2Fself-service%2F%3Futm_source%3Dceo%26utm_medium%3Dtop%26utm_campaign%3Dself&__ts=1666072925251"
driver = webdriver.Chrome(executable_path=r'C:\Users\SEC\chromedriver')
# driver.get(url = URL)




# requesting HTML and parsing it
# main_p = requests.get(URL)
# soup = BeautifulSoup(main_p.text, "html.parser")


# main page
# ID_input = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/form/div[1]/span/input').click()


# log in

wb = pd.read_excel(r'C:\Users\SEC\Coding\VScode\crawling\store_list.xls')
login = LogInfo()
shape_df = wb.shape[0]
error_list = []

for i in range(0, shape_df):
    try:
        driver.get(url = URL)
        main_p = driver.page_source
        soup = BeautifulSoup(main_p, "html.parser")
        ID_input = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/form/div[1]/span/input').click()
        webdriver.ActionChains(driver).send_keys(login.get_bmid(i)).perform()
        time.sleep(1.5)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(login.get_bmpw(i)).perform()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/form/button').click()
        time.sleep(1)
        if driver.current_url == r'https://ceo.baemin.com/self-service/?utm_source=ceo&utm_medium=top&utm_campaign=self':
            ceo_p = driver.page_source
            soup2 = BeautifulSoup(ceo_p, "html.parser") # renewing HTML
            time.sleep(1.5)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button/i').click() # order page
            time.sleep(1.5)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/nav/ul/li[6]/ul/li[2]/a').click()  # settlement
            time.sleep(1.5)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/div[1]/div/div[1]/button[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/form/div[2]/div/div[1]/div/div/select[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/form/div[2]/div/div[1]/div/div/select[2]/option[10]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/form/div[3]/button/i').click()
            time.sleep(1.5)
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/form/div[1]/div[1]/button').click()
            time.sleep(1.5)
            driver.get(url = r'https://ceo.baemin.com/')
            time.sleep(1.5)
            ceo_p = driver.page_source
            soup2 = BeautifulSoup(ceo_p, "html.parser") # renewing HTML
            driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[2]/span[5]/a').click()
            time.sleep(1)
            
        else:
            error_list.append(i)
            print(i, 'error')
    except:
        error_list.append(i)
        print(i, 'error')

driver.close()