### main modules ###
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

### sub-modules ###
from bs4 import BeautifulSoup
import pandas as pd
import random
import time
import sys
sys.path.append(r'.\crawling')

### my modules ###
from yogiyo.LogYGY import LogProcess


class ScrapeSales(LogProcess):
    def __init__(self, app):
        super().__init__(app)
        self.url = r'https://owner.yogiyo.co.kr/owner/orders/'
        
    
    def parse_page(self, driver):
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        return soup
        

    def select_store(self, driver, store_index):
        this_name = self.getStore(store_index)
        WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="selectedStore"]/div[1]/button')
        )).click()
        name_list = driver.find_elements(By.CLASS_NAME, 'name')
        
        for name in range(len(name_list)):
            if '프랭크' and this_name[:2] in name_list[name].text:
                this_store = name_list[name]
        try:
            this_store.click()
        except:
            y_result = self.make_frame(self, store_index)
            return y_result
    
    
    def select_date(self, driver, start, end):
        ran_num = round(random.random())
        time.sleep(ran_num)
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="start_date"]')))
        driver.execute_script(f"document.getElementById('start_date').setAttribute('value', '{start}')")
        driver.execute_script(f"document.getElementById('end_date').setAttribute('value', '{end}')")
        driver.find_element(By.XPATH, '//*[@id="orders-filters-form"]/div[2]/button').click()
        
    
    def scrapeSales(self, driver, store_index):
        sale_y = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/table/tbody/tr/td[2]/div/strong').text
        qt_y = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/table/tbody/tr/td[1]/div/strong').text
        sale_y = sale_y.replace(',', '').replace('원', '')
        sale = int(sale_y)
        qt_y = qt_y.replace(',', '').replace('건', '')
        qt = int(qt_y)
        store = self.getStore(store_index)
        merge = [store_index, store, sale, qt]
        empty = []
        empty.append(merge)
        y_result = pd.DataFrame(empty, columns= self.columns)
        return y_result
    
    
    def tips_YGY(self, driver, tips:bool):
        if tips == True:
            soup = self.parse_page(driver)
            tags = soup.find_all('tr')
            tip = list(tags[-1])[5].text
            tip = int(tip.replace(',', ''))
            return tip