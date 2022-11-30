### Main modules ###
from selenium import webdriver
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


class LogIn(LogInfo):
    def __init__(self, app):
        super().__init__(self, app)
        self.log_btn = '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/a'
        self.log_out = '//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[2]/span[4]/a'
        self.input_box = '//*[@id="root"]/div[1]/div/div[2]/form/div[1]/span/input'
        self.confirm = '//*[@id="root"]/div[1]/div/div[2]/form/button'
        self.pop_up = '//*[@id="root"]/dialog/header/button'
        self.self_service = '//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[1]/span[1]'
        self.url_self = 'https://ceo.baemin.com/self-service'
        self.url_main = 'https://ceo.baemin.com/'


    def login(self, driver, store_index):
        ran_num = round(random.random(), 2)
        driver.page_source
        driver.find_element(By.XPATH, self.log_btn).click() # log_in button in main page
        time.sleep(ran_num + 0.5)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.input_box))).click() # ID input box
        time.sleep(ran_num)
        webdriver.ActionChains(driver).send_keys(self.getBmid(store_index)).perform()
        time.sleep(ran_num + 0.3)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(self.getBmpw(store_index)).perform()
        time.sleep(ran_num + 0.3)
        driver.find_element(By.XPATH, self.confirm).click()  # confirm button


    def bridge_path(self, driver):
        ran_num = round(random.random(), 2)
        
        try:
            time.sleep(ran_num + 0.3)
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
                (By.XPATH, self.pop_up))).click()        # wait for popup
        except:
            pass
    
        try:
            time.sleep(ran_num + 0.3)
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
                (By.XPATH, self.self_service))).click()      # click self service
        except:
            time.sleep(ran_num + 0.3)
            driver.get(self.url_self)
        
        time.sleep(ran_num + 0.5)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 3).until(EC.url_contains('self-service'))


    def close_windows(self, driver):
        if len(driver.window_handles) > 1:
            for windows in range(1, len(driver.window_handles)):
                driver.switch_to.window(driver.window_handles[windows])
                time.sleep(1)
                driver.close()      # close all of new taps
            driver.switch_to.window(driver.window_handles[0])
            
            try:
                WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
                    (By.XPATH, self.pop_up))).click()        # wait for popup
            except:
                pass

            time.sleep(0.5)        
            driver.find_element(By.XPATH, self.log_out).click()  # log out
            time.sleep(0.5)
        else:
            driver.get(self.url_main)
            driver.page_source
        
            try:
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
                    (By.XPATH, self.pop_up))).click()        # wait for popup
            except:
                pass
            
            time.sleep(0.5)
            driver.find_element(By.XPATH, self.log_out).click()  # log out
            time.sleep(0.5)



#functions below are going to be removed


### basic data ###
wb = pd.read_excel(r'.\crawling\common\store_list.xls')
df_storelist = pd.DataFrame(wb)
df_storelist.fillna("", inplace=True)
df_storelist.set_index('store')



### log in ###
def logIn(driver, log_info, store_index):
    ran_num = round(random.random(), 2)
    driver.page_source
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div[2]/div[1]/a').click() # log_in button in main page
    xpath = '//*[@id="root"]/div[1]/div/div[2]/form/div[1]/span/input'
    
    time.sleep(ran_num + 0.5)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath))).click() # ID input box
    time.sleep(ran_num)
    webdriver.ActionChains(driver).send_keys(log_info.getBmid(store_index)).perform()
    time.sleep(ran_num + 0.3)
    webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(log_info.getBmpw(store_index)).perform()
    time.sleep(ran_num + 0.3)
    driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/form/button').click()  # confirm button
    
    return driver.page_source



### Move to self service page ###
def bridgePath(driver):
    pop_up = '//*[@id="root"]/dialog/header/button'
    self_service = '//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[1]/span[1]'
    ran_num = round(random.random(), 2)
        
    try:
        time.sleep(ran_num + 0.3)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, pop_up))).click()        # wait for popup
    except:
        pass
    
    try:
        time.sleep(ran_num + 0.3)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, self_service))).click()      # click self service
    except:
        time.sleep(ran_num + 0.3)
        driver.get(r'https://ceo.baemin.com/self-service')
    
    time.sleep(ran_num + 0.5)
    driver.switch_to.window(driver.window_handles[-1])
    
    WebDriverWait(driver, 3).until(EC.url_contains('self-service'))
    
    return driver.page_source



### log out ###
def closeWindows(driver):
    ran_num = round(random.random(), 2)
    pop_up = '//*[@id="root"]/dialog/header/button'
    
    if len(driver.window_handles) > 1:
        
        for windows in range(1, len(driver.window_handles)):
            driver.switch_to.window(driver.window_handles[windows])
            time.sleep(ran_num)
            driver.close()                                        # close all of new-taps

        driver.switch_to.window(driver.window_handles[0])
       
        try:
            time.sleep(ran_num + 1)
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, pop_up))).click()        # wait for popup
        except:
            pass
        
        time.sleep(ran_num + 0.5)        
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[2]/span[4]/a').click()  # log out
        time.sleep(ran_num + 0.5)
    
    else:
        driver.get(r'https://ceo.baemin.com/')
        driver.page_source
        
        try:
            time.sleep(ran_num + 0.3)
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, pop_up))).click()        # wait for popup
        except:
            pass
        
        time.sleep(ran_num + 0.5)
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[2]/span[4]/a').click()  # log out
        time.sleep(ran_num + 0.5)