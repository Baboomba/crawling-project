import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
data = DataProcess(kind='tips')
error = ErrorProcess(kind='tips')
scrape = ScrapeData(kind='tips')


def exist_store(store_index):
    if info.getYgyid(store_index) == '':
        return False
    else:
        return True


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
                if login.log_check_new(driver) == True:
                    pass
                else:
                    try:
                        driver.page_source
                        WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
                            (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/button')
                        )).click()   # alert mail
                        driver.page_source
                        WebDriverWait(driver, 1.5).until(EC.element_to_be_clickable(
                            (By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/button')
                        )).click()   # alert mail
                        time.sleep(1)
                    except:
                        login.log_old(driver, store_index)
                        if login.log_check_old(driver) == True:
                            pass
                        else:
                            continue
                if driver.current_url == 'https://ceo.yogiyo.co.kr/approval/list':
                    continue
                driver.get(r'https://owner.yogiyo.co.kr/owner/orders/')
                time.sleep(1.5)
                scrape.parse_page(driver)
                scrape.select_store(driver, store_index)
                scrape.select_date(driver,
                                   start='2022-11-01',
                                   end='2022-11-30')
                result_tips = scrape.scrape_tips(driver, store_index)
                yogiyo_tips = data.result_process(yogiyo_tips, result_tips)
                save.save_data(yogiyo_tips,
                               app='yogiyo',
                               kind='tips',
                               period='month')
                login.log_out(driver)
                
            except:
                error_result = error.error_list(store_index, kind='tips')
                yogiyo_tips = data.result_process(yogiyo_tips, error_result)
                login.log_out(driver)
    driver.quit()