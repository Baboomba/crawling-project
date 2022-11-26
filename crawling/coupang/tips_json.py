import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

import requests
import json

from bs4 import BeautifulSoup

import time


option = webdriver.ChromeOptions()
option.add_argument('headless')



#  setting url
URL = r"https://ceo.baemin.com/web/login?returnUrl=https%3A%2F%2Fceo.baemin.com%2Fself-service%2F%3Futm_source%3Dceo%26utm_medium%3Dtop%26utm_campaign%3Dself&__ts=1666072925251"
driver = webdriver.Chrome(executable_path=r'C:\Users\SEC\chromedriver')


# defining class for log information
wb = pd.read_excel(r'C:\Users\SEC\Coding\VScode\crawling\store_list.xls')
df = pd.DataFrame(wb)
df.fillna("", inplace=True)


# getting id/pw in the store list
class log_info:
    
    def get_bmid(self, i):
        bmid = df.iloc[i][2]
        return bmid
    
    def get_bmpw(self, i):
        bmpw = df.iloc[i][3]
        return bmpw



# log in
login = log_info()
shape_df = wb.shape[0]


# creating dataframe for tips
df['tips'] = ''


try:
    for i in range(0, shape_df):
        driver.get(url = URL)
        main_p = driver.page_source
        soup = BeautifulSoup(main_p, "html.parser")
        ID_input = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/form/div[1]/span/input').click()
        webdriver.ActionChains(driver).send_keys(login.get_bmid(i)).perform()
        time.sleep(1.5)
        webdriver.ActionChains(driver).key_down(Keys.TAB).send_keys(login.get_bmpw(i)).perform()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/form/button').click()
        time.sleep(1.5)
        tips = []
    
        if driver.current_url == r'https://ceo.baemin.com/self-service/?utm_source=ceo&utm_medium=top&utm_campaign=self':
        
            time.sleep(1)
            for num in list(range(0, 7)):
                URL2 = r'https://self.baemin.com/v1/settle/history/details?page={}&size=10&startDate=2022-10-01&endDate=2022-10-31'.format(num)
                driver.get(url = URL2)
                p_source = driver.page_source
                soup = BeautifulSoup(p_source, "html.parser")
                parcing = soup.select_one('pre').text
                j_obj = json.loads(parcing)  # transforming into json obj.
            
                if j_obj['totalSize'] != 0:
        
                    for l in range(len(j_obj['contents'])):
                        j_melt = j_obj['contents'][l]['salesAmount']['baeminDeliveryTipAmountDetails']
                        for m in range(len(j_melt)):
                            tip = list(j_melt[m].values())
                            tips.append(tip[-1])     # the value, tips
            
                time.sleep(1.3)
                
            df['tips'][i] = sum(tips)
            
            driver.get(r'https://ceo.baemin.com/')
            main_p = driver.page_source
            soup = BeautifulSoup(main_p, "html.parser")
            driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[2]/span[5]/a').click()
        
        

        else:
            df['tips'][i] = 'log_error'        
            print(i, 'log_error')

    df.to_excel('tips.xlsx')

    driver.close()

except:
    df.to_excel('tips.xlsx')