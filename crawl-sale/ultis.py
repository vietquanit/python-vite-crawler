from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def settingDriver():
    # Khởi tạo trình điều khiển của trình duyệt
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    s = Service('/Users/vietquan/Documents/chromedriver')
    driver = webdriver.Chrome(options=options, service=s)
    return driver
    
def openBrowser(driver, url):
    if driver.session_id is not None:
        driver.implicitly_wait(10)
        driver.get(url)# Lấy nội dung HTML của trang web
        html_content = driver.page_source
        # Sử dụng BeautifulSoup để phân tích cú pháp HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    else:
        driver.implicitly_wait(10)
        driver.get(url)# Lấy nội dung HTML của trang web
        html_content = driver.page_source
        # Sử dụng BeautifulSoup để phân tích cú pháp HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    return soup

def closeBrowser(driver):
    driver.close()

def quitBrowser(driver):
    driver.quit()
