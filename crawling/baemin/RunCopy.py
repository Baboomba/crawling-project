import pandas as pd
import time

import sys
sys.path.append(r'.\crawling')

from common.DriverSet import driver_chrome
from common.Log_info import LogInfo, storeSize
from baemin.LogBM import LogProcess_BM
from baemin.path import FindPath
from baemin.sale.getSale import ScrapeSales
from baemin.Exception import ErrorProcess
from common.Save import SaveData
from baemin.tip.get_tip import GetTips


def scrapeBM(headless:bool):
    info = LogInfo(app='baemin')
    login = LogProcess_BM()
    path = FindPath()
    scrape = ScrapeSales(app='baemin')
    Tip = GetTips(app='baemin', start='2022-11-01', end='2022-11-30')
    error = ErrorProcess(app='baemin')
    save = SaveData(app='baemin', kind='sales')
    
    URL = r'https://ceo.baemin.com/'
    driver = driver_chrome(headless=headless)
    driver.get(URL)
    store_num = storeSize()
    
    for store_index in range(0, store_num):
        try:
            if driver.current_url == URL:
                
                login.main_page(driver)
                login.login(driver, store_index)
                if login.log_check(driver) == True:
                    pass
                else:
                    continue
                
                #     try:
                #         login.check_pass(driver)
                #     except:
                #         pass
                # else:
                #     continue

                login.popup_close(driver)
                login.self_service_click(driver)
                path.check_category(driver)
                path.path_adjust(driver)
                path.path_order(driver)
                scrape.calandar_click(driver)
                scrape.select_yesterday(driver)
                df_result = scrape.frame_result(driver, store_index)
                df_sales = save.sales_day(store_index, df_result)
                # scrape.calandar_click(driver)
                # scrape.select_month(driver)
                # df_result_m = scrape.frame_result(driver, store_index)
                # df_month = save.sales_month(store_index, df_result_m)
                # df_result_t = Tip.frame_tip(driver, store_index)
                # df_tips = save.tip_bm(store_index, df_result_t)
                login.check_window(driver)
                login.logout(driver)                
                
            else:
                driver.get(URL)
                time.sleep(1)
                if driver.current_url == URL:
                    continue
                break
        except:
            print('error in ' + '{}'.format(store_index) + 'th store')
            df_error = error.sales_error(store_index)
            df_sales = save.sales_day(store_index, df_error)
            #df_month = save.sales_month(store_index, df_error)
            # df_error_t = error.tip_error(store_index)
            # df_tips = save.tip_bm(store_index, df_error_t)
            login.check_window(driver)
            if driver.current_url == URL:
                login.logout(driver)
            else:
                break
            
    df_sales.set_index('No.', drop=True, inplace=True)
    df_sales.fillna("", inplace=True)
    df_sales.to_excel(save.data_dir_day)
    #df_month.set_index('No.', drop=True, inplace=True)
    #df_month.fillna("", inplace=True)
    #df_month.to_excel(save.data_dir_month)
    # df_tips.set_index('No.', drop=True, inplace=True)
    # df_tips.fillna('', inpalce=True)
    # df_tips.to_excel(save.data_dir_tip)
    
    driver.quit()




if __name__ == '__main__':
    scrapeBM(headless=False)
    print('complete')