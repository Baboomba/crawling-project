### Main modules ###
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

### Additional Modules ###
import random
import time

### My modules ###
from common.Log_info import LogInfo

import pandas as pd

class LogProcess(LogInfo):
    
    def __init__(self):
        self.url_new = r'https://ceo.yogiyo.co.kr/login?by_dowant=1'
        self.url_old = r'https://owner.yogiyo.co.kr/owner/login/'
        self.url_sucess = r'https://owner.yogiyo.co.kr/owner/?login=1'
        self.frame = pd.DataFrame(
            index=range(0, 1),
            columns= ['No.', 'store', 'sales', 'qt']
        )
        
                
    def log_new(self, driver, store_index):
        ran_num = round(random.random())
        driver.get(self.url_new)
        time.sleep(ran_num + 0.3)
        driver.page_source
        WebDriverWait(driver, ran_num).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="username"]')
            )
        ).click()
        webdriver.ActionChains(driver).send_keys(self.getYgyid(store_index)).perform()
        time.sleep(ran_num + 0.3)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(self.getYgypw(store_index)).perform()
        time.sleep(ran_num + 0.3)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/form/button').click()
        time.sleep(ran_num + 1)
                
    
    def log_old(self, driver, store_index):
        ran_num = round(random.random())
        driver.get(self.log_old)
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
        
        
    def make_frame(self, store_index):
        empty = []
        store = self.getStore(store_index)
        error = [store_index, store, '', '']
        empty.append(error)
        y_result = pd.DataFrame(empty, columns= ['No.', 'store', 'sales', 'qt'])
        return y_result


    def log_check(self, driver, store_index, make_frame):
        if driver.current_url == self.url_sucess:
            pass
        else:
            y_result = make_frame(self, store_index)
            return y_result