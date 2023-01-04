import selenium
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup



def count_pin(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select('.font-weight-medium')

    for index, card in enumerate(cards):
        if card.text == '오픈리스트':
            num = 4 + index
            pin = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div[3]/div[2]/div[1]/div[{num}]/div[2]/table/tbody').text
            pin_num = pin.count("진행중")
            print(pin_num)
        else:
            pass