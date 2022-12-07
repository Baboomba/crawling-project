import sys
sys.path.append(r'.\crawling')
import time

### my modules ###
from common.DriverSet import DriverSet
from common.Database import DataProcess
from common.Log_info import LogInfo
from common.Exception import ErrorProcess
from common.Save import SaveData
from yogiyo.LogYGY import LogProcess
from yogiyo.ygy_sales import ScrapeData


login = LogProcess(kind='tips')
Driver = DriverSet()
info = LogInfo()
save = SaveData()
data = DataProcess('tips')
error = ErrorProcess('tips')


def exist_store(store_index):
    if info.getYgyid(store_index) == '':
        return False
    else:
        return True


def yogiyo_login(driver, store_index):
    login.main_page(driver)
    login.log_new(driver, store_index)
    if login.log_check(driver) == False:
        login.log_old(driver, store_index)
        if login.log_check(driver) == False:
            return False
    else:
        return True
        

def yogiyo_target(driver, store_index, start, end):
    driver.page_source
    date = ScrapeData(app='yogiyo')
    date.select_store(driver, store_index)
    date.select_date(driver, start, end)
    
    
def yogiyo_scrape_sales(driver, store_index):
    data = ScrapeData()
    process = DataProcess(kind='sales')
    sales = data.scrape_sales(driver, store_index)
    global yogiyo_sales
    if store_index < 1:
        yogiyo_sales = process.make_frame(kind='sales')
        yogiyo_sales = process.result_process(yogiyo_sales, sales)
    else:
        yogiyo_sales = process.result_process(yogiyo_sales, sales)
    return yogiyo_sales


def yogiyo_scrape_tips(driver, store_index):
    data = ScrapeData()
    process = DataProcess(kind='tips')
    sales = data.scrape_sales(driver, store_index)
    global yogiyo_tips
    if store_index < 1:
        yogiyo_tips = process.make_frame(kind='tips')
        yogiyo_tips = process.result_process(yogiyo_tips, sales)
    else:
        yogiyo_tips = process.result_process(yogiyo_tips, sales)
    return yogiyo_tips
        
    
    

if __name__ == '__main__':
    driver = Driver.debug_run()
    size = info.store_size()
    yogiyo_tips = data.make_frame(kind='tips')

    for store_index in range(size):
        if exist_store(store_index) == False:
            continue
        else:
            try:
                login.main_page(driver)
                login.log_new(driver, store_index)
                login.log_check(driver)
                if login.log_check_new == True:
                    pass
                else:
                    login.log_old(driver, store_index)
                    if login.log_check_old == True:
                        pass
                    else:
                        continue
                time.sleep(1.5)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                if yogiyo_login(driver, store_index) == True:
                    time.sleep(1)
                    driver.get(url='https://owner.yogiyo.co.kr/owner/orders/')
                else:
                    continue
                yogiyo_target(driver, store_index,
                            start='2022-11-01',
                            end='2022-11-30')
                tip_scraped = yogiyo_scrape_tips(driver, store_index)
                yogiyo_tips = data.result_process(yogiyo_tips, tip_scraped)
                save.save_data(yogiyo_tips,
                            app='yogiyo',
                            kind='tips',
                            period='month')
                
            except:
                error = ErrorProcess(kind='tips')
                error_occured = error.error_list(store_index, kind='tips')
                yogiyo_tips = data.result_process(yogiyo_tips, error_occured)
                save.save_data(yogiyo_tips,
                            app='yogiyo',
                            kind='tips',
                            period='month')
                print(f'{store_index}th store error')
            
            finally:
                login.log_out(driver)
                continue
    
    save.set_index(yogiyo_tips)
    driver.quit()
    print('complete')