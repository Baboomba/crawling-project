### Main modules ###
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### Additional modules ###
import pandas as pd
import random
import time

import sys
sys.path.append(r'.\crawling')

### My modules ###
from common.Log_info import LogInfo


### basic data ###
wb = pd.read_excel(r'.\crawling\common\store_list.xls')
df_storelist = pd.DataFrame(wb)
df_storelist.fillna("", inplace=True)
df_storelist.set_index('store')


### log in ###
class LogProcess_BM(LogInfo):
    def __init__(self):
        super().__init__()
        self.log_btn = '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/a'
        self.log_out = '//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[2]/span[4]/a'
        self.input_box = '//*[@id="root"]/div[1]/div/div/form/div[1]/span/input'
        self.confirm = '//*[@id="root"]/div[1]/div/div/form/button'
        self.next_btn = '//*[@id="root"]/div[1]/div[1]/div/div/form/div[2]/a/span'
        self.pop_up = '//*[@id="root"]/dialog/header/button'
        self.self_service = '//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[1]/span[1]'
        self.url_self = 'https://ceo.baemin.com/self-service'
        self.url_main = 'https://ceo.baemin.com/'
        self.url_pass = '//*[@id="root"]/div[1]/div[1]/div/div[2]/div/span/a'
        self.ran_num = round(random.random(), 2)
        
    
    def main_page(self, driver):
        driver.page_source
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, self.log_btn)
        )).click()
        time.sleep(self.ran_num + 1)
    
    
    def login(self, driver, store_index):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
            (By.XPATH, self.input_box))).click() # ID input box
        time.sleep(self.ran_num)
        webdriver.ActionChains(driver).send_keys(
            self.getBmid(store_index)).perform()
        time.sleep(self.ran_num + 0.3)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(
            self.getBmpw(store_index)).perform()
        time.sleep(self.ran_num + 1)
        driver.find_element(By.XPATH, self.confirm).click()  # confirm button
        

    def pass_change(self, driver):
        try:
            WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable((By.XPATH, self.next_btn))).click()   # 비밀번호 변경 안내 문구
        except:
            pass
    
    
    def biz_uni(self, driver):    # 통합회원 수락 페이지
        try:
            WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/form/ul/li/div/label/section/span')
            )).click()
            time.sleep(1)
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/form/button')
            )).click()
        except:
            pass
        

    def log_check(self, driver):
        time.sleep(self.ran_num + 0.5)
        if driver.current_url == self.url_main:
            return True
        else:
            return False
    
    
    def alert_close(driver):
        try:
            time.sleep(1)
            Alert(driver).accept()
        except:
            pass
    
        
    def popup_close(self, driver):
        try:
            time.sleep(self.ran_num + 0.5)
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
                (By.XPATH, self.pop_up))).click()
            time.sleep(self.ran_num + 0.5)
        except:
            pass
        
        
    def self_service_click(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, self.self_service))).click()
        time.sleep(self.ran_num)
    
    
    def check_window(self, driver):
        if len(driver.window_handles) > 1:
            for windows in range(1, len(driver.window_handles)):
                driver.switch_to.window(driver.window_handles[windows])
                time.sleep(self.ran_num)
                driver.close()     # close all of new-taps
        else:
            pass
        driver.switch_to.window(driver.window_handles[0])
        return driver.page_source
    
    
    def logout(self, driver):
        time.sleep(0.5)        
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, self.log_out)
        )).click()
        time.sleep(self.ran_num + 0.5)
    
    
    def logout_another(self, driver):  # 단순 경로용 로그아웃
        link = '//*[@id="root"]/div/header/div[2]/a[2]'   # 우상단 이름 버튼
        logout = '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div/div[1]/div[2]/a'
        driver.find_element(By.XPATH, link).click()
        time.sleep(self.ran_num + 1)
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, logout)
        )).click()
        time.sleep(self.ran_num*2)