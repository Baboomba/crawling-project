from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time

import random

import sys
sys.path.append(r'C:\Users\SEC\Coding\VScode\crawling')



def findPath(driver, path):
    ran_num = round(random.random(), 2)
    category_button = '//*[@id="root"]/div/div[2]/button'
    order_tab = '//*[@id="root"]/div/div[3]/div[1]/nav/div/ul[7]/li[1]/a/span'
    review_tab = '//*[@id="root"]/div/div[3]/div[1]/nav/div/ul[3]/li[1]/a/span'
    
    try:
        WebDriverWait(driver, ran_num + 1).until(EC.element_to_be_clickable((By.XPATH, category_button))).click()  # categoty button
    except:
        pass
    
    time.sleep(ran_num + 0.5)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/nav/div/ul[5]/li[2]/a/span').click()  # pay ads tab
    time.sleep(ran_num + 0.5)
    
    if path == 'review':
        webdriver.ActionChains(driver).key_down(Keys.PAGE_UP).perform()
        time.sleep(ran_num + 0.5)
        driver.find_element(By.XPATH, review_tab).click()
    else:
        webdriver.ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
        time.sleep(ran_num + 0.5)
        driver.find_element(By.XPATH, order_tab).click()
    
    time.sleep(ran_num + 0.5)
    
    return driver.page_source