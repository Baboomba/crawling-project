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


def scrape_tips(headless:bool):
    info = LogInfo()
    login = LogProcess_BM()
    path = FindPath()
    scrape = ScrapeSales()
    Tip = GetTips(start='2022-11-01', end='2022-11-30')
    error = ErrorProcess(kind='tips')
    save = SaveData()
    data = DataProcess(kind='tips')
    Driver = DriverSet()
    
    URL = r'https://ceo.baemin.com/'
    driver = Driver.driver_for_cp()
    driver.get(URL)
    size = info.store_size()
    global result_tips
    result_tips = data.make_frame(kind='tips')
    
    
    for store_index in range(0, size):
        try:
            login.main_page(driver)
            login.login(driver, store_index)
            if login.log_check(driver) == True:
                pass
            else:
                driver.get(URL)
                continue
            #login.alert_close(driver)
            login.popup_close(driver)
            login.self_service_click(driver)
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[-1])
            scraped = Tip.list_tips(driver, store_index)
            result_tips = data.result_process(result_tips, scraped)
            save.save_data(result_tips,
                            app='baemin',
                            kind='tips',
                            period='month')
            login.check_window(driver)
            login.logout(driver)
            
        except:
            print(f'error in {store_index}th store')
            scraped_error = error.tip_error(store_index)
            result_tips = data.result_process(result_tips, scraped_error)
            save.save_data(result_tips,app='baemin',kind='tips',period='month')
            login.check_window(driver)
            continue
    
    result_tips = save.set_index(result_tips)
    save.save_data(result_tips, app='baemin', kind='tips', period='month')
    
    driver.quit()
    

if __name__ == '__main__':
    scrape_tips(headless=False)
    print('complete')