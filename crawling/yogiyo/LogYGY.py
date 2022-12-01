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

class LogProcess(LogInfo):
    def __init__(self, app):
        super().__init__(app)
        self.url_main = r'https://owner.yogiyo.co.kr/owner/'
        self.url_new = r'https://ceo.yogiyo.co.kr/login?by_dowant=1'
        self.url_old = r'https://owner.yogiyo.co.kr/owner/login/'
        self.url_sucess = r'https://owner.yogiyo.co.kr/owner/orders/'
        self.frame = pd.DataFrame(
            index=range(0, 1),
            columns= self.columns
        )
        self.pass_first = '//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/button'
        self.pass_second = '//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/button'
    
    
    def main_page(self, driver):
        ran_num = round(random.random())
        driver.get(self.url_main)
        time.sleep(ran_num + 0.3)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/a[1]/button')
        )).click()
        
                
    def log_new(self, driver, store_index):
        ran_num = round(random.random())
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/form/div[1]/div/div[2]/div[2]/input')
        )).click()
        webdriver.ActionChains(driver).send_keys(self.getYgyid(store_index)).perform()
        time.sleep(ran_num + 0.3)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(self.getYgypw(store_index)).perform()
        time.sleep(ran_num + 0.3)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/form/button').click()
        time.sleep(ran_num + 1)
                
    
    def log_old(self, driver, store_index):
        ran_num = round(random.random())
        driver.get(self.url_old)
        time.sleep(ran_num + 0.3)
        driver.page_source
        WebDriverWait(driver, ran_num).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))
        ).click()
        webdriver.ActionChains(driver).send_keys(self.getYgyid(store_index)).perform()
        time.sleep(ran_num + 0.3)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(self.getYgypw(store_index)).perform()
        time.sleep(ran_num + 0.3)
        driver.find_element(By.XPATH, '//*[@id="login"]/form/fieldset/div[4]/button').click()
        time.sleep(ran_num)
        
        
    def make_frame(self, store_index, value:str):
        empty = []
        store = self.getStore(store_index)
        error = [store_index, store, value, '']
        empty.append(error)
        y_result = pd.DataFrame(empty, columns= self.columns)
        return y_result


    def log_check(self, driver):
        time.sleep(2)
        if driver.current_url == self.url_sucess:
            return True
        else:
            return False
        
    
    def log_out(self, driver):
        ran_num = round(random.random())
        driver.get('https://owner.yogiyo.co.kr/owner/')
        WebDriverWait(driver, ran_num + 0.3).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="nav"]/div/ul[2]/li[5]/a'))
        ).click()
        time.sleep(ran_num + 0.5)
        Alert(driver).accept()
        time.sleep(2)