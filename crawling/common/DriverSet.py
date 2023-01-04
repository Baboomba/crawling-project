from selenium import webdriver
from subprocess import Popen
from fake_useragent import UserAgent
import sys
sys.path.append(r'./')


class DriverSet:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        self.driver_dir = r'./chromedriver'
        self.download_path=r'./result'
        self.debug_port = r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"'
    
    
    def debug_run(self):
        Popen(self.debug_port)
        options = webdriver.ChromeOptions()
        # options.add_argument('--no-sandbox')
        # options.add_argument("disable-gpu")
        # options.add_argument("--lang=ko_KR")
        # options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_argument("--disable-extensions")
        # options.add_experimental_option('useAutomationExtension', False)
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('user-agent='+f'{self.user_agent}')
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(executable_path=self.driver_dir, options=options)
        return driver
    
    
    def driver_for_cp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        user_ag = UserAgent().random
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})
        driver = webdriver.Chrome('chromedriver.exe', options=options)

        # 크롤링 방지 설정을 undefined로 변경
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    })
                    """
        })
        return driver
    
    
    def driver_option(self, headless=False):
        options = webdriver.ChromeOptions()
        ua = UserAgent()
        user_agent = ua.random
        options.add_argument(f'user-agent={self.user_agent}')
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
        if headless == True:
            options.add_argument('headless')
            options.add_argument("window-size=1920,1080")
        else:
            options.add_argument('--start-maximized')
        return options
    
    
    def driver_run(self, headless=False):
        options = self.driver_option(headless)
        driver = webdriver.Chrome(executable_path=self.driver_dir, options=options)
        return driver


    def set_proxy(self):
        PROXY = "211.53.100.186:8080" # IP:Port
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "proxyType": "MANUAL"
            }
    
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True
        driver = self.driver_run(headless=False)
        return driver
    
    
    def enable_download(self, driver):
        driver.command_executor._commands["send_command"] = (
        "POST", '/session/$sessionId/chromium/send_command'
        )
    
        params = {
            'cmd': 'Page.setDownloadBehavior',
            'params': {
                'behavior': 'allow',
                'downloadPath': self.download_path
            }
        }
    
        driver.execute("send_command", params)