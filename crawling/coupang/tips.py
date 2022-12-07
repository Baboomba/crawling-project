import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
sys.path.append(r'.\crawling')
import time

### my modules ###
from common.DriverSet import DriverSet
from common.Log_info import LogInfo



URL = r"https://store.coupangeats.com/merchant/login"


class ScrapeTip(LogInfo):
    def __init__(self):
        super().__init__()
        self.input_box = '//*[@id="loginId"]'
        self.confirm_btn = '//*[@id="merchant-login"]/div/div[2]/div/div/div/form/button'
        self.url_login = r"https://store.coupangeats.com/merchant/login"
        self.logout_path = '//*[@id="merchant-management"]/div/div/header/div[1]/a[2]'
        self.logout_btn = '//*[@id="merchant-management"]/div/div/header/div[1]/a[1]/ul/li[2]/a/span'
    
    
    def log_in(self, driver, store_index):
        time.sleep(1)
        driver.page_source
        driver.find_element(By.XPATH, '//*[@id="loginId"]').clear()
        WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, self.input_box)
        )).click()
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        webdriver.ActionChains(driver).send_keys(self.getCpid(store_index)).perform()
        time.sleep(0.5)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(
            self.getCppw(store_index)).perform()
        time.sleep(0.5)
        driver.find_element(By.XPATH, self.confirm_btn).click()
        time.sleep(1)
    
        
        
    def extract_store_num(self, driver):
        current_url = driver.current_url
        store_num = current_url[-6:]
        return store_num
    
    
    def path_sales(self, driver):
        store_num = self.extract_store_num(driver)
        url_sales = rf'https://store.coupangeats.com/merchant/management/orders/{store_num}'
        driver.get(url_sales)
        time.sleep(1)
        
        
    def download_tips(self, driver, date:str):
        store_num = self.extract_store_num(driver)
        url_tips = rf'https://store.coupangeats.com/api/v1/merchant/web/emails?type=salesOrder&action=download&downloadRequestDate={date}&storeId={store_num}'
        driver.get(url_tips)
        time.sleep(1)
    
    
    def logout(self, driver):
        driver.find_element(By.XPATH, self.logout_path).click()
        time.sleep(1)
        driver.find_element(By.XPATH, self.logout_btn).click()
        time.sleep(1)
        


        
        
if __name__ == '__main__':
    Driver = DriverSet()
    scrape = ScrapeTip()
    info = LogInfo()
    
    driver = Driver.driver_for_cp()
    driver.get(r'https://store.coupangeats.com/')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="merchant-intro"]/div/div[1]/div/div/div/div[2]/a[2]').click()
    size = info.store_size()
    
    for store_index in range(0, size):
        if info.getCpid(store_index) == ('' or None):
            continue
        try:
            scrape.log_in(driver, store_index)
            if driver.current_url == scrape.url_login:
                continue
            time.sleep(1.5)
            scrape.path_sales(driver)
            time.sleep(1.5)
            scrape.download_tips(driver, date='2022-11')
            time.sleep(1.5)
            scrape.logout(driver)
        except:
            print(f'{store_index}th store error')
            driver.get(scrape.url_login)
            time.sleep(1)
    print('complete')