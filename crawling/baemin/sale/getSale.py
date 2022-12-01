### Setup Modules ###

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import sys
sys.path.append(r'.\crawling')

import time
import pandas as pd
import random

from common.Log_info import LogInfo

class ScrapeSales(LogInfo):
    def __init__(self):
        super().__init__(self)
        self.calandar = '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[1]/button[1]/div/p[2]'
        self.tab_day = '//*[@id="root"]/div/div[4]/div[1]/form/div[2]/div/div/div[1]/label[1]/div'
        self.tab_month = '//*[@id="root"]/div/div[4]/div[1]/form/div[2]/div/div/div[1]/label[2]/div'
        self.radio_yesterday = '//*[@id="root"]/div/div[4]/div[1]/form/div[2]/div/div/div[2]/div/div/div[2]/label/input'
        self.radio_prev_month = '//*[@id="root"]/div/div[4]/div[1]/form/div[2]/div/div/div[2]/div/div/div[2]/label/input'
        self.confirm = '//*[@id="root"]/div/div[4]/div[1]/form/div[3]/button'
        self.data_sales = '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[2]/div[2]/span[2]/b'
        self.data_quantity = '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[2]/div[1]/span[2]/b'
        self.ran_num = round(random.random(), 2)
        
        
    def calandar_click(self, driver):
        webdriver.ActionChains(driver).key_down(Keys.PAGE_UP).perform()
        time.sleep(self.ran_num + 0.5)
        webdriver.ActionChains(driver).key_down(Keys.PAGE_UP).perform()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, self.calandar)
        )).click()
        
        
    def select_yesterday(self, driver):
        driver.find_element(By.XPATH, self.tab_day).click()
        time.sleep(self.ran_num + 0.1)
        driver.find_element(By.XPATH, self.radio_yesterday).click()
        time.sleep(self.ran_num + 0.1)
        driver.find_element(By.XPATH, self.confirm).click()
        time.sleep(self.ran_num + 0.1)
        
        
    def select_month(self, driver):
        driver.find_element(By.XPATH, self.tab_month).click()
        time.sleep(self.ran_num + 0.3)
        driver.find_element(By.XPATH, self.radio_prev_month).click()
        time.sleep(self.ran_num + 0.3)
        driver.find_element(By.XPATH, self.confirm).click()
        time.sleep(self.ran_num + 0.3)


    def scrape_sales(self, driver):
        time.sleep(self.ran_num + 0.2)
        sale_str = driver.find_element(By.XPATH, self.data_sales).text # scrape sale
        sale = int(sale_str.replace(',', ''))
        return sale


    def scrape_quantity(self, driver):
        time.sleep(self.ran_num + 0.2)
        qt_str = driver.find_element(By.XPATH, self.data_quantity).text
        qt = int(qt_str.replace(',', ''))
        return qt
    
    
    def frame_result(self, driver, store_index):
        store_name = self.getStore(store_index)
        empty = []
        sale = self.scrape_sales(driver)
        qt = self.scrape_quantity(driver)
        empty.append([store_index, store_name, sale, qt])
        df_result = pd.DataFrame(empty, index=range(0, 1), columns = self.sales_columns)
        return df_result





### Scrape sales ###
def scrapeSales(driver, log_info, store_index):
    ran_num = round(random.random(), 2)
    webdriver.ActionChains(driver).key_down(Keys.PAGE_UP).perform()
    time.sleep(ran_num + 0.5)
    webdriver.ActionChains(driver).key_down(Keys.PAGE_UP).perform()
       
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[1]/button[1]/div/p[2]')
        )
    )   # wait for calandar
    
    time.sleep(ran_num)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[1]/button[1]/div/p[2]').click() # calandar click
    time.sleep(ran_num)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/form/div[2]/div/div/div[1]/label[1]/div').click()  # select tab(day.week)
    time.sleep(ran_num)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/form/div[2]/div/div/div[2]/div/div/div[2]/label/input').click()  # select yesterday
    time.sleep(ran_num)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/form/div[3]/button').click()  # confirm
    time.sleep(ran_num)
    webdriver.ActionChains(driver).key_down(Keys.PAGE_UP).perform()
    time.sleep(ran_num)
    sale_str = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[2]/div[2]/span[2]/b').text # scrape sale
    sale = int(sale_str.replace(',', ''))
    qt_str = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[2]/div[1]/span[2]/b').text  # scrape quantity
    qt = int(qt_str.replace(',', ''))
        
    store_name = log_info.getStore(store_index)
    empty = []
    empty.append([store_index, store_name, sale, qt])
    df_result = pd.DataFrame(empty, index=range(0, 1), columns = [['No.','store', 'baemin', 'baemin', ], ['', '', 'sales', 'quantity']])
    
    return df_result


def scrapeSales_month(driver, log_info, store_index):
    ran_num = round(random.random())
    time.sleep(ran_num)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[1]/button[1]/div/p[2]').click() # calandar click
    time.sleep(ran_num)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/form/div[2]/div/div/div[1]/label[2]/div').click()  #select tab(month)
    time.sleep(ran_num)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/form/div[2]/div/div/div[2]/div/div/div[2]/label/input').click()  # select prev-month
    time.sleep(ran_num)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/form/div[3]/button').click()  # confirm
    time.sleep(ran_num)
    webdriver.ActionChains(driver).key_down(Keys.PAGE_UP).perform()
    time.sleep(ran_num)
    sale_str = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[2]/div[2]/span[2]/b').text # scrape sale
    sale = int(sale_str.replace(',', ''))
    qt_str = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[2]/div[1]/span[2]/b').text  # scrape quantity
    qt = int(qt_str.replace(',', ''))
        
    store_name = log_info.getStore(store_index)
    empty = []
    empty.append([store_index, store_name, sale, qt])
    df_result = pd.DataFrame(empty, index=range(0, 1), columns = [['No.','store', 'baemin', 'baemin', ], ['', '', 'sales', 'quantity']])
    
    return df_result