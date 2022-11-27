from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd

import sys
sys.path.append(r'.\crawling')

from common.DriverSet import driver_chrome
from common.Log_info import LogInfo, storeSize
from common.Save import dataDir, saveSales
from LogBM import logIn, bridgePath, closeWindows
from path import findPath
from sale.getSale import scrapeSales
from Exception import errorProcess


def scrapeBM(headless:bool):
    URL = r'https://ceo.baemin.com/'
    log_info = LogInfo()
    driver = driver_chrome(headless=headless)
    driver.get(URL)
    data_dir = dataDir(app='baemin', kind='sale')
    store_num = storeSize()

    for store_index in range(0, store_num):
        try:
            if driver.current_url == URL:
                
                try:
                    logIn(driver, log_info, store_index)       # log in sucess or failure
                    WebDriverWait(driver, 2).until_not(EC.url_contains('login'))
                except TimeoutException:
                    df_result = errorProcess(store_index, log_info, kind='sale')
                    df_sales = saveSales(store_index, df_result, app='baemin', kind='sale')
                    driver.get(URL)
                    continue
                    
                bridgePath(driver)
                findPath(driver, path='order')  # scrape sales data
                df_result = scrapeSales(driver, log_info, store_index)
                df_sales = saveSales(store_index, df_result, app='baemin', kind='sale')
                
                closeWindows(driver)
            else:
                closeWindows(driver)
                break
                        
        except:
            print('error in ' + '{}'.format(store_index) + 'th store')
            df_result = None
            df_result = errorProcess(store_index, log_info, kind='sale')
            df_sales = saveSales(store_index, df_result, app='baemin', kind='sale')
            closeWindows(driver)
        
    df_sales.set_index('No.', drop=True, inplace=True)
    df_sales.fillna("", inplace=True)
    df_sales.to_excel(data_dir)
    driver.quit()



if __name__ == '__main__':
    scrapeBM(headless=True)
    print('complete')