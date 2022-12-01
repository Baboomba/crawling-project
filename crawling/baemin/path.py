from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time

import random

import sys
sys.path.append(r'.\crawling')



class FindPath:
    def __init__(self):
        self.ran_num = round(random.random(), 2)
        self.category_button = '//*[@id="root"]/div/div[2]/button'
        self.order_tab = '//*[@id="root"]/div/div[3]/div[1]/nav/div/ul[7]/li[1]/a/span'
        self.review_tab = '//*[@id="root"]/div/div[3]/div[1]/nav/div/ul[3]/li[1]/a/span'
        self.home_tab = '//*[@id="root"]/div/div[3]/div[1]/nav/div/ul[1]/li/a/span'
        self.tip_tab = '//*[@id="root"]/div/div[3]/div[1]/nav/div/ul[7]/li[2]/a/span'


    def check_category(self, driver):
        time.sleep(self.ran_num)
        driver.switch_to.window(driver.window_handles[-1])
        try:
            WebDriverWait(driver, self.ran_num + 0.5).until(EC.element_to_be_clickable(
                (By.XPATH, self.category_button))).click()
        except:
            pass


    def path_adjust(self, driver):
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, self.review_tab))).click()
        time.sleep(self.ran_num)


    def path_order(self, driver):
        webdriver.ActionChains(driver).key_down(Keys.PAGE_DOWN).perform()
        time.sleep(self.ran_num + 0.3)
        driver.find_element(By.XPATH, self.order_tab).click()
        time.sleep(self.ran_num)
        return driver.page_source
        
        
    def path_review(self, driver):
        webdriver.ActionChains(driver).key_down(Keys.PAGE_UP).perform()
        time.sleep(self.ran_num + 0.3)
        driver.find_element(By.XPATH, self.review_tab).click()
        time.sleep(self.ran_num)
        return driver.page_source
        
        

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