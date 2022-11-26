import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import pandas as pd

import urllib
import requests

from bs4 import BeautifulSoup

import time

import openpyxl

from fake_useragent import UserAgent


ua = UserAgent(use_cache_server=True)
ua.random

options = Options()
options.add_argument('user-agent=%s'%ua)


URL = r"https://store.coupangeats.com/"
driver = webdriver.Chrome(executable_path=r'C:\Users\SEC\chromedriver', options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
            """
})


# log in

class log_info:
    
    def get_cpid(self, i):
        cpid = df.iloc[i][6]
        return cpid
    
    def get_cppw(self, i):
        cppw = df.iloc[i][7]
        return cppw


    

wb = pd.read_excel(r'C:\Users\SEC\Coding\VScode\crawling\store_list.xls')
df = pd.DataFrame(wb)
login = log_info()
shape_df = wb.shape[0]
error_list = []

for i in range(0, shape_df):
    try:

        time.sleep(1.5)
        driver.get(url = URL)   # main page
        main_p = driver.page_source
        soup = BeautifulSoup(main_p, "html.parser")
        driver.find_element(By.XPATH, '//*[@id="merchant-intro"]/div/div[1]/div/div/div/div[2]/a[2]').click()
        time.sleep(1)
        main_p = driver.page_source
        soup = BeautifulSoup(main_p, "html.parser")
        log_click = driver.find_element(By.XPATH, '//*[@id="loginId"]')
        log_click.click()
        log_click.send_keys(Keys.CONTROL, 'a')
        log_click.send_keys(Keys.DELETE)
        log_click.click()
        webdriver.ActionChains(driver).send_keys(login.get_cpid(i)).perform()
        time.sleep(1.5)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(login.get_cppw(i)).perform()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="merchant-login"]/div/div[2]/div/div/div/form/button').click()   # log in

        if driver.current_url != URL:
            time.sleep(3)
            ceo_p = driver.page_source
            soup2 = BeautifulSoup(ceo_p, "html.parser") # renewing HTML
            try:
                time.sleep(2)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[3]/div/div/div/button').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div/div/div/button').click()


                driver.find_element(By.XPATH, '//*[@id="merchant-management"]/div/nav/div[2]/ul/li[2]/a/span[2]').click() # order page
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-management"]/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/button/span').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[1]/div/div[2]/div/div/div').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[1]/div/div[2]/div/div/ul/li/a').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div/div/ul/li[3]/a').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div').click()
                time.sleep(1)            
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/ul/li[10]/a').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[4]/button[2]/span').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[1]/button/span').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-management"]/div/div/header/div[1]/a[2]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-management"]/div/div/header/div[1]/a[1]/ul/li[2]/a/span').click()
                time.sleep(1)
                    
                                
            except:
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div/div/div/button').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="merchant-management"]/div/nav/div[2]/ul/li[2]/a/span[2]').click() # order page
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-management"]/div/div/div[2]/div[1]/div/div/div/div[1]/div[1]/button/span').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[1]/div/div[2]/div/div/div').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[1]/div/div[2]/div/div/ul/li/a').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/div/div/ul/li[3]/a').click()
                time.sleep(0.5)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div').click()
                time.sleep(1)            
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/ul/li[10]/a').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[4]/button[2]/span').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-onboarding-body"]/div[2]/div[3]/div/div[1]/button/span').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-management"]/div/div/header/div[1]/a[2]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="merchant-management"]/div/div/header/div[1]/a[1]/ul/li[2]/a/span').click()
                time.sleep(1)

                
        else:
            error_list.append(i)
            print(i, 'log error')
            
    except:
        driver.close()
        driver = webdriver.Chrome(executable_path=r'C:\Users\SEC\chromedriver', options=options)
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
            """
})
        
        
print('complete')