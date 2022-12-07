from selenium import webdriver
from subprocess import Popen
from fake_useragent import UserAgent
import sys
sys.path.append(r'.\crawling')


class DriverSet:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        self.driver_dir = r'.\crawling\chromedriver'
        self.download_path=r'.\crawling\result'
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
        


# from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
# from fake_headers import Headers
# import requests

# class RANDOM_PROXY:
#     def proxy_create(self):
#         """
#         무작위로 프록시를 생성해서 가져오는 코드
#         """
#         self.req_proxy = RequestProxy()
#         proxy = self.test_proxy() # 잘 작동되는 프록시 선별
#         return proxy

#     def test_proxy(self):
#         """
#         가져온 프록시중에서 실제로 작동되는 프록시만 하나씩 가져오는 코드
#         test_url : 자신의 IP를 확인하는 코드. 여기서 변경된 IP가 나오면 성공적으로 우회가된것
#         """
#         test_url = 'http://ipv4.icanhazip.com' 
#         while True: # 제대로된 프록시가 나올때까지 무한반복 
#             requests = self.req_proxy.generate_proxied_request(test_url)

#             if requests is not None:
#                 print("\t Response: ip={0}".format(u''.join(requests.text).encode('utf-8')))
#                 proxy = self.req_proxy.current_proxy
#                 break

#             else:
#                 continue
                
#         return proxy # 잘작동된 proxy를 뽑아준다. 
        
#     def crawling(self):
#        header = Headers(
#                     browser="chrome",  # Generate only Chrome UA
#                     os="win",  # Generate ony Windows platform
#                     headers=True  # generate misc headers
#                 )
#        self.headers = header.generate() # 랜덤 유저 에이전트를 생성해주는 함수.
#        _url = ''
       
#        self.proxies = {} # request.get 인자에 넣어줄 딕셔너리 생성 
#        self.proxies['http'] = 'http://%s' % self.proxy
       
#        html = self.session.get(_url, headers=self.headers,proxies=self.proxies).content
#        # get 인자에 프록시와 헤더를 넣어주면 끝.
       

