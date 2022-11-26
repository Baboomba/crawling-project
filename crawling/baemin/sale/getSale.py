### Driver Settings ###

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import time
import pandas as pd
import random


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
    time.sleep(ran_num + 0.5)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/form/div[2]/div/div/div[1]/label[1]/div').click()  # select tab(day.week)
    time.sleep(ran_num + 0.5)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/form/div[2]/div/div/div[2]/div/div/div[2]/label/input').click()  # select yesterday
    time.sleep(ran_num + 0.5)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/form/div[3]/button').click()  # confirm
    time.sleep(ran_num + 1)
    webdriver.ActionChains(driver).key_down(Keys.PAGE_UP).perform()
    time.sleep(ran_num + 0.5)
    sale = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[2]/div[2]/span[2]/b').text # scrape sale
    qt = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[2]/div[1]/span[2]/b').text  # scrape quantity
    
    store_name = log_info.getStore(store_index)
    empty = []
    empty.append([store_index, store_name, sale, qt])
    df_result = pd.DataFrame(empty, index=range(0, 1), columns = [['No.','store', 'baemin', 'baemin', ], ['', '', 'sales', 'quantity']])
    
    return df_result