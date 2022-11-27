from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from bs4 import BeautifulSoup

import datetime
import time

import urllib

import pandas as pd

import random

from common.Log_info import LogInfo



def selectStore(driver):
    ran_num = round(random.random(), 2)
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div[1]/div')
        )
    )      # select store / just wait. don't click it.
    
    time.sleep(ran_num + 0.5)
    store_name = driver.find_elements(By.TAG_NAME, 'option')
    for name in range(0, len(store_name)):
        if '배달의민족' in store_name[name].text and '프랭크' in store_name[name].text:
            store_name[name].click()
    
    return time.sleep(ran_num + 0.5)



### find date of the Review ###

def dateForm(start_date):
    date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    transDate = date.strftime('%a %b %d %Y')
    return transDate

    

def findDate(driver, start, end):
    ran_num = round(random.random(), 2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="review-page"]/div[2]/div/div/button'))).click() # calandar button
            
    while True:
        day_picker = driver.find_elements(By.CLASS_NAME, 'DayPicker-Day')
        empty = []
        
        for start_date in range(0, len(day_picker)):
            date_List = day_picker[start_date].get_attribute("aria-label")
            empty.append(date_List)
        
        if start not in empty:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="review-page"]/div[2]/div/div/div/div/div[2]/div/div[1]/span[2]'))).click()
            time.sleep(ran_num + 1)
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="review-page"]/div[2]/div/div/div/div/div[2]/div/div[1]/span[2]')))
            time.sleep(ran_num + 1)
            day_picker[empty.index(start)].click()
            day_picker = driver.find_elements(By.CLASS_NAME, 'DayPicker-Day')  # Because, calandar has changed, repeat needed
            empty = []
            
            for start_date in range(0, len(day_picker)):      # repeating clicking the same date for initialization
                date_List = day_picker[start_date].get_attribute("aria-label")
                empty.append(date_List)
            
            time.sleep(ran_num)
            day_picker[empty.index(start)].click()
            break
    
        
    while True:
        day_picker = driver.find_elements(By.CLASS_NAME, 'DayPicker-Day')
        empty = []
                
        for end_date in range(0, len(day_picker)):
            date_List = day_picker[end_date].get_attribute("aria-label")
            empty.append(date_List)
        
        if end not in empty:
            time.sleep(ran_num + 0.5)
            driver.find_element(By.XPATH, '//*[@id="review-page"]/div[2]/div/div/div/div/div[2]/div/div[1]/span[2]').click()
            time.sleep(ran_num)
        else:
            time.sleep(ran_num)
            day_picker[empty.index(end)].click()
            break
    
    time.sleep(ran_num)
    calandar = driver.find_element(By.XPATH, '//*[@id="review-page"]/div[2]/div/div/button')
    return driver.execute_script("arguments[0].click();", calandar)



### Scrape Reviews ###

def scrollDown(driver, seconds):
    ran_num = round(random.random(), 2)
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=seconds)
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(ran_num + 1)
        if datetime.datetime.now() > end:
            break



def scrapeReview(driver, store_index):
    ran_num = round(random.random(), 2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    card = soup.select('.Card')
    review = []
        
    for cards in range(1, len(card)):
        
        rate = soup.select_one('#review-page > div.review-wrap > div > div:nth-child({}) > div.user-info > div.rating-stars-wrap > div'.format(cards))
        
        if rate == None:
            continue
        else:
            rate = rate.text
            rate = int(rate)
        
        written_day = soup.select_one('#review-page > div.review-wrap > div > div:nth-child({}) > div.user-info > div.rating-stars-wrap > span'.format(cards))
        
        if rate > 5 or written_day.text != '어제':
            continue
        
        nick = soup.select_one('#review-page > div.review-wrap > div > div:nth-child({}) > div.user-info > div.rating-stars-wrap > p'.format(cards))
        view = soup.select_one('#review-page > div.review-wrap > div > div:nth-child({}) > div.review-info > p'.format(cards))
        
        if nick == None:
            nick = ''
        else:
            nick = nick.text
        
        if view == None:
            view = ''
        else:
            view = view.text
                
        try:
            img  = WebDriverWait(driver, ran_num).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, '#review-page > div.review-wrap > div > div:nth-child({}) > div.review-info > div:nth-child(2) > ul > li:nth-child(1)'.format(cards))
                    )
                ).value_of_css_property("background-image")
            img_url = img[5:-2]
            urllib.request.urlretrieve(img_url, r'.\crawling\download\baemin_img\{}_{}.jpg'.format(store_index, cards))
            img_no = '{}_{}'.format(store_index, cards)
            
        except TimeoutException or NoSuchElementException:
            img_url = ''
            img_no = ''
        
        log_info = LogInfo()
        store = log_info.getStore(store_index)
        merge = [store, nick, rate, view, img_url, img_no]
        review.append(merge)
        df_Result = pd.DataFrame(review, columns=['store', 'nick', 'rate', 'view', 'img url', 'img_no'])
    
    return df_Result