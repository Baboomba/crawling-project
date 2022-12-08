import pandas as pd
import time

import sys
sys.path.append(r'.\crawling')

from common.DriverSet import DriverSet
from common.Log_info import LogInfo
from baemin.LogBM import LogProcess_BM
from baemin.path import FindPath
from baemin.sale.getSale import ScrapeSales
from baemin.Exception import ErrorProcess
from common.Save import SaveData
from baemin.tip.get_tip import GetTips
from common.Database import DataProcess


def scrapeBM(headless:bool):
    info = LogInfo()
    login = LogProcess_BM()
    path = FindPath()
    scrape = ScrapeSales()
    Tip = GetTips(start='2022-11-01', end='2022-11-30')
    error = ErrorProcess(kind='sales')
    save = SaveData()
    data = DataProcess(kind='sales')
    Driver = DriverSet()
    
    URL = r'https://ceo.baemin.com/'
    driver = Driver.debug_run()
    driver.get(URL)
    size = info.store_size()
    global result_sales
    result_sales = data.make_frame(kind='sales')
    
    
    for store_index in range(0, size):
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
            #login.alert_close(driver)
            login.popup_close(driver)
            login.self_service_click(driver)
            path.check_category(driver)
            path.path_adjust(driver)
            path.path_order(driver)
            scrape.calandar_click(driver)
            scrape.select_yesterday(driver)
            scraped = scrape.list_sales(driver, store_index)
            result_sales = data.result_process(result_sales, scraped)
            save.save_data(result_sales,
                            app='baemin',
                            kind='sales',
                            period='day')
            login.check_window(driver)
            login.logout(driver)
            
        except:
            print(f'error in {store_index}th store')
            scraped_error = error.sales_error(store_index)
            result_sales = data.result_process(result_sales, scraped_error)
            save.save_data(result_sales,app='baemin',kind='sales',period='day')
            login.check_window(driver)
            if driver.current_url == URL:
                login.logout(driver)
            else:
                break
    
    result_sales = save.set_index(result_sales)
    save.save_data(result_sales, app='baemin', kind='sales', period='day')
    
    driver.quit()




if __name__ == '__main__':
    scrapeBM(headless=False)
    print('complete')