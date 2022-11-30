import sys
sys.path.append(r'.\crawling')

### my modules ###
from common.DriverSet import driver_chrome
from common.Log_info import storeSize
from common.Save import SaveData
from yogiyo.LogYGY import LogProcess
from yogiyo.ygy_sales import ScrapeSales


def scrapeYGY(start:str, end:str, tips:bool, headless:bool):
    _logIn = LogProcess(app='yogiyo')
    _save = SaveData(app='yogiyo', kind='sales')
    scrape = ScrapeSales(app='yogiyo')
    driver = driver_chrome(headless=headless)
    store_num = storeSize()

    for store_index in range(0, store_num):
        try:
            if (_logIn.getYgyid(store_index) == None) or (_logIn.getYgyid(store_index) == ''):
                continue
            
            _logIn.main_page(driver)
            _logIn.log_new(driver, store_index)

            if _logIn.log_check(driver) == True:
                pass
            else:
                _logIn.log_old(driver, store_index)

                if _logIn.log_check(driver) == True:
                    pass
                else:
                    y_result = _logIn.make_frame(store_index, value='error')
                    _save.sales(store_index, y_result)
                    continue
        
            scrape.select_store(driver, store_index)
            scrape.select_date(driver, start, end)
            y_result = scrape.scrapeSales(driver, store_index)
            _save.sales(store_index, y_result)
            scrape.tips_YGY(driver, tips)
            _logIn.log_out(driver)
        
        except:
            y_result = _logIn.make_frame(store_index, value='error')
            _save.sales(store_index, y_result)
            _logIn.log_out(driver)
        
    _save.set_index()    
    driver.quit()
            

if __name__ == '__main__':
    from baemin import RunCopy
    RunCopy.scrapeBM(headless=False)
    scrapeYGY(start='2022-11-20', end='2022-11-28', tips=False, headless=False)