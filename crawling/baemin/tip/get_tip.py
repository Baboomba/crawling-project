### Main Modules ###
from selenium import webdriver
from selenium.webdriver.common.by import By

### Additional Modules ###
import json
import pandas as pd
import random
import sys
sys.path.append(r'.\crawling')
import time

### My Modules ###
from common.Log_info import LogInfo



class GetTips(LogInfo):
    def __init__(self, app, start:str, end:str):
        super().__init__(app)
        #self.calandar = '//*[@id="root"]/div/div[3]/div[2]/div[1]/div/div[2]/button/div/p[2]'
        self.data_settle = '/html/body/pre'
        self.start = start
        self.end = end
        self.ran_num = round(random.random())
    
    
    def connect_api(self, driver, page_no:int):
        api_tips = f'https://self.baemin.com/v1/settle/history/details?page=0{page_no}&size=10&startDate={self.start}&endDate={self.end}'
        driver.get(api_tips)
        time.sleep(self.ran_num)
        settle = driver.find_element(By.XPATH, self.data_settle).text
        return settle
    
    
    def trans_json(self, driver, page_no):
        settle = self.connect_api(driver, page_no)
        j_obj = json.loads(settle)
        return j_obj
    
    
    def parse_json(self, j_obj):    # it can parse only one page
        empty = []
        for i in range(len(j_obj['contents'])):
            tip = j_obj['contents'][i]['delivery']['baeminDeliveryTipAmount']['total']
            empty.append(tip)
        tips = sum(empty)
        return tips
    
    
    def get_tip(self, driver):
        empty = []
        for page_no in range(0, 10):
            time.sleep(self.ran_num + 0.5)
            j_obj = self.trans_json(driver, page_no)
            if j_obj['totalSize'] != 0:
                tips = self.parse_json(j_obj)
                empty.append(tips)
            else:
                break
        tip = sum(empty)
        return tip
    
    
    def frame_tip(self, driver, store_index):
        store_name = self.getStore(store_index)
        empty = []
        tip = self.get_tip(driver)
        empty.append([store_index, store_name, tip])
        df_result = pd.DataFrame(empty, index=range(0, 1), columns = self.tip_columns)
        return df_result