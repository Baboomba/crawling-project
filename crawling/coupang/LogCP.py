### Main modules ###
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

### Additional Modules ###
import random
import time
import sys
sys.path.append(r'.\crawling')

### My modules ###
from common.Log_info import LogInfo

import pandas as pd

class LogCP(LogInfo):
    def __init__(self, app):
        super().__init__(app)
        self.url_main = r'https://store.coupangeats.com/'
        self.url_sucess = r'https://store.coupangeats.com/merchant/management/settlement'
        self.frame = pd.DataFrame(
            index=range(0, 1),
            columns= self.columns
        )
    
    
    def main_page(self, driver):
        ran_num = round(random.random())
        driver.get(self.url_main)
        time.sleep(ran_num + 0.3)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="merchant-intro"]/div/div[1]/div/div/div/div[2]/a[2]')
        )).click()
        
                
    def log_in(self, driver, store_index):
        ran_num = round(random.random())
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="loginId"]')
        )).click()
        webdriver.ActionChains(driver).send_keys(self.getCpid(store_index)).perform()
        time.sleep(ran_num + 0.3)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(self.getCppw(store_index)).perform()
        time.sleep(ran_num + 0.3)
        driver.find_element(By.XPATH, '//*[@id="merchant-login"]/div/div[2]/div/div/div/form/button').click()
        time.sleep(ran_num + 1)
        
        
    def make_frame(self, store_index, value:str):
        empty = []
        store = self.getStore(store_index)
        error = [store_index, store, value, '']
        empty.append(error)
        y_result = pd.DataFrame(empty, columns= self.columns)
        return y_result


    def log_check(self, driver):
        time.sleep(2)
        if self.url_sucess in driver.current_url:
            return True
        else:
            return False
        
    
    def log_out(self, driver):
        ran_num = round(random.random())
        driver.get()
        WebDriverWait(driver, ran_num + 0.3).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="merchant-management"]/div/div/header/div[1]/a[2]'))
        ).click()
        WebDriverWait(driver, ran_num + 0.3).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="merchant-management"]/div/div/header/div[1]/a[1]/ul/li[2]/a/span'))
        ).click()
        time.sleep(ran_num + 0.5)
        
        
        
        
        