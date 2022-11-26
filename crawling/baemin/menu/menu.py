import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

import json

from bs4 import BeautifulSoup

import time


option = webdriver.ChromeOptions()
option.add_argument('headless')


#  setting url
URL = r"https://ceo.baemin.com/web/login?returnUrl=https%3A%2F%2Fceo.baemin.com%2Fself-service%2F%3Futm_source%3Dceo%26utm_medium%3Dtop%26utm_campaign%3Dself&__ts=1666072925251"
driver = webdriver.Chrome(executable_path=r'C:\Users\SEC\chromedriver')


# defining class for log information
wb = pd.read_excel(r'C:\Users\SEC\Coding\VScode\crawling\store_list(menu).xls')
df = pd.DataFrame(wb)
df.fillna("", inplace=True)


class log_info:
    
    def get_bmid(self, i):
        bmid = df.iloc[i][2]
        return bmid
    
    def get_bmpw(self, i):
        bmpw = df.iloc[i][3]
        return bmpw
    
    def get_cpid(self, i):
        cpid = df.iloc[i][6]
        return cpid
    
    def get_cppw(self, i):
        cppw = df.iloc[i][7]
        return cppw
    
    
# log in
login = log_info()
shape_df = wb.shape[0]
shop_no = [202112060435, 201903150217, 202202220276]

# creating dataframe for tips

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
        quantity = []
    
        if driver.current_url == r'https://ceo.baemin.com/self-service/?utm_source=ceo&utm_medium=top&utm_campaign=self':
            time.sleep(1)
            
            
            URL2 = r'https://self.baemin.com/v1/orders?orderStatus=CLOSED&offset=00&limit=10&startDate=2022-10-01&endDate=2022-11-06&shopNumbers=&shopOwnerNumber={}'.format(shop_no[i])
            driver.get(URL2)
            p_source = driver.page_source
            soup = BeautifulSoup(p_source, "html.parser")
            parcing = soup.select_one('pre').text
            j_obj = json.loads(parcing)
            k = 0
            time.sleep(1)
        
            while j_obj['contents'] != []:
            
                URL3 = r'https://self.baemin.com/v1/orders?orderStatus=CLOSED&offset={}0&limit=10&startDate=2022-10-01&endDate=2022-11-06&shopNumbers=&shopOwnerNumber={}'.format(k, shop_no[i])
                driver.get(URL3)
                p_source = driver.page_source
                soup = BeautifulSoup(p_source, "html.parser")
                parcing = soup.select_one('pre').text
                j_obj = json.loads(parcing)
                                
                for l in range(len(j_obj['contents'])):
                    list_empty = []
                    goods_date = j_obj['contents'][l]['order']['orderDateTime']
                    list_empty.append(goods_date)
                    goods_quantity = j_obj['contents'][l]['order']['items']
                    for m in range(len(goods_quantity)):
                        extract = goods_quantity[m]
                        q_list = list(extract.values())[:-2]
                        total_list = list_empty + q_list
                        quantity.append(total_list)
                                
                k = k + 1
                time.sleep(1)
            
                df_q = pd.DataFrame(quantity)
                                
            df_q.to_excel(r'menu_quantity_{}.xlsx'.format(i))            
            driver.get(r'https://ceo.baemin.com/')
            main_p = driver.page_source
            soup = BeautifulSoup(main_p, "html.parser")
            driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/div/div[2]/span[5]/a').click()
            time.sleep(1.5)
            
        else:
            print('log error')
        
    driver.close

except:
    df_q.to_excel(r'menu_quantity(error).xlsx')
    print('except error')