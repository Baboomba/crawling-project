from selenium import webdriver

import sys
sys.path.append(r'.\crawling')

def driver_chrome(headless = False):

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    driver_dir = r'.\crawling\chromedriver'
    download_path=r'.\crawling\result'
    options = webdriver.ChromeOptions()
    
    if headless == True:
        options.add_argument('headless')
        options.add_argument("window-size=1920,1080")
        options.add_argument('user-agent='+'{}'.format(user_agent))
        
    else:
        options.add_argument('--start-maximized')
    
    # options.add_experimental_option('prefs', {
    #     'download.default_directory' : download_path,
    #     'download.prompt_for_download' : False,
    # })
    
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    driver_path = driver_dir
    chrome = webdriver.Chrome(executable_path = driver_path, options = options)
    
    return chrome



def enable_download(driver):
    download_path = r'.\crawling\result'  # check
    
    driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command'
        )
    
    params = {
        'cmd': 'Page.setDownloadBehavior',
        'params': {
            'behavior': 'allow',
            'downloadPath': download_path
        }
    }
    
    driver.execute("send_command", params)