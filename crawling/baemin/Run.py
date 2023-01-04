import pandas as pd
import time

import sys
sys.path.append(r'./')

from common.DriverSet import DriverSet
from common.Log_info import LogInfo
from baemin.LogBM import LogProcess_BM
from baemin.path import FindPath
from baemin.getSale import ScrapeSales
from baemin.Exception import ErrorProcess
from common.Save import SaveData
from common.Database import DataProcess




def scrapeBM_min_path(headless:bool, time:str, save_dir:str):
    info = LogInfo()
    login = LogProcess_BM()
    path = FindPath()
    scrape = ScrapeSales()
    error = ErrorProcess(kind='sales')
    save = SaveData()
    data = DataProcess(kind='sales')
    Driver = DriverSet()
    
    URL = r'https://ceo.baemin.com/'
    driver = Driver.driver_run(headless)
    driver.get(URL)
    size = info.store_size()
    global result_sales
    result_sales = data.make_frame(kind='sales')
    
    
    for store_index in range(0, size):
        global progress
        progress = store_index
        try:
            login.main_page(driver)
            login.login(driver, store_index)
            login.pass_change(driver)
            login.biz_uni(driver)
            if login.log_check(driver) == True:
                pass
            else:
                driver.get(URL)
                continue
            path.simple_path(driver)
            
            if time == 'yesterday':
                scrape.calandar_click(driver)
                scrape.select_yesterday(driver)
                scraped = scrape.list_sales(driver, store_index)
                result_sales = data.result_process(result_sales, scraped)
                result_sales.to_excel(save_dir)
                login.logout_another(driver)
            else:
                scrape.calandar_click(driver)
                scrape.select_month(driver)
                scraped = scrape.list_sales(driver, store_index)
                result_sales = data.result_process(result_sales, scraped)
                result_sales.to_excel(save_dir)
                login.logout_another(driver)
            
        except:
            print(f'error in {store_index}th store')
            scraped_error = error.sales_error(store_index)
            result_sales = data.result_process(result_sales, scraped_error)
            result_sales.to_excel(save_dir)
            driver.quit()
            driver = Driver.driver_run(headless)
            driver.get(URL)
    
    result_sales = save.set_index(result_sales)
    result_sales.to_excel(save_dir)
    
    driver.quit()