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
from common.Database import DataProcess

import pandas as pd

class LogProcess(LogInfo, DataProcess):
    def __init__(self, kind:str):
        LogInfo.__init__(self)
        DataProcess.__init__(self, kind)
        self.url_main = r'https://owner.yogiyo.co.kr/owner/'
        self.url_new = r'https://ceo.yogiyo.co.kr/login?by_dowant=1'
        self.url_old = r'https://owner.yogiyo.co.kr/owner/login/'
        self.url_sucess = r'https://owner.yogiyo.co.kr/owner/orders/'
        self.frame = pd.DataFrame(
            index=range(0, 1),
            columns= self.columns
        )
        self.input_first = '//*[@id="root"]/div/div[1]/div/div/form/div[1]/div/div[2]/div[2]/input'
        self.input_second = '//*[@id="username"]'
        self.confirm_first = '//*[@id="root"]/div/div[1]/div/div/form/button'
        self.confirm_second = '//*[@id="login"]/form/fieldset/div[4]/button'
        self.ran_num = round(random.random())
    
    
    def main_page(self, driver):
        time.sleep(self.ran_num + 0.3)
        driver.get(self.url_main)
        WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div[1]/div[2]/div/div[2]/div/a[1]/button')
        )).click()
    
    
    def login_action(self, driver, store_index, input_path:str):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, input_path)
        )).click()
        webdriver.ActionChains(driver).send_keys(self.getYgyid(store_index)).perform()
        time.sleep(self.ran_num + 0.3)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(
            self.getYgypw(store_index)).perform()
        time.sleep(self.ran_num + 0.3)
        
                
    def log_new(self, driver, store_index):
        input_path = self.input_first
        self.login_action(driver, store_index, input_path)
        driver.find_element(By.XPATH, self.confirm_first).click()
        time.sleep(1)
                        
    
    def log_old(self, driver, store_index):
        ran_num = round(random.random())
        driver.get(self.url_old)
        time.sleep(ran_num + 0.3)
        input_path = self.input_second
        self.login_action(driver, store_index, input_path)
        driver.find_element(By.XPATH, self.confirm_second).click()
        time.sleep(1)
        try:
            Alert(driver).accept()
        except:
            pass
                
        
    def log_check_new(self, driver):
        time.sleep(1)
        if driver.current_url == self.url_sucess:
            return True
        else:
            return False
        
        
    def log_check_old(self, driver):
        time.sleep(1)
        if driver.current_url != (self.url_old or self.url_new):
            return True
        else:
            return False
    
    
    def log_out(self, driver):
        ran_num = round(random.random())
        driver.get('https://owner.yogiyo.co.kr/owner/')
        try:
            WebDriverWait(driver, ran_num + 0.3).until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="nav"]/div/ul[2]/li[5]/a'))
                ).click()
        except:
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="nav"]/div/ul[2]/li[4]/a')
            )).click()
        time.sleep(ran_num + 0.5)
        Alert(driver).accept()
        time.sleep(0.5)