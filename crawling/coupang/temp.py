from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)



### schedule tag ###
schedule = '//*[@id="merchant-management"]/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[1]'
left = '//*[@id="merchant-management"]/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[2]/div[1]/div[1]/div/input'
right = '//*[@id="merchant-management"]/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div/input'


driver.find_element(By.XPATH, schedule).click()
driver.find_element(By.XPATH, left).click()
driver.find_element(By.XPATH, right).click()


prev = driver.find_element(By.CLASS_NAME, "DayPicker-NavButton--prev").click()  # 달력 넘기기
next = driver.find_element(By.CLASS_NAME, "DayPicker-NavButton--next").click()


aaa = driver.find_elements(By.CLASS_NAME, 'DayPicker-Day') # 해당 일자 검색
for i in range(len(aaa)):
    if aaa[i].text == '10':
        aaa[i].click()   # 해당 클릭


### date info ###
left_tag = '//*[@id="merchant-management"]/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[2]/div[1]/div[1]/div/input'  # 왼쪽 달력
date_left = driver.find_element(By.XPATH, left_date).get_attribute('value')
right_tag = '//*[@id="merchant-management"]/div/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div/input' # 오른쪽 달력
date_right = driver.find_element(By.XPATH, right_date).get_attribute('value')



### calculate date ###
class TransTime:
    def __init__(self, form):
        self.form_date = datetime.strptime(form, "%Y.%m.%d")
        self.month = datetime.strftime(self.form_date, "%m")





# download excel of tips
# https://store.coupangeats.com/api/v1/merchant/web/emails?type=salesOrder&action=download&downloadRequestDate=2022-10&storeId=465336