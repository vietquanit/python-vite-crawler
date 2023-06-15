from email.mime import image
from importlib.resources import path
import pathlib
from posixpath import split
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from ultis import createFileJsonData, checkFolderAndCreateNew
from PIL import Image
import os 
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import random

def main():
    # Khởi tạo trình điều khiển của trình duyệt
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    s = Service('/Users/vietquan/Documents/chromedriver')
    driver = webdriver.Chrome(options=options, service=s)

    #url crawling
    domain = 'https://www.nettruyenplus.com'
    urlFilter = domain + '/tim-truyen'
    urlTopDay = domain + '/tim-truyen?status=-1&sort=13'
    urlTopWeek = domain + '/tim-truyen?status=-1&sort=12'
    urlTopMonth = domain + '/tim-truyen?status=-1&sort=11'
    urlTopMonth = domain + '/tim-truyen?status=-1&sort=30'
    arrUrlTopManga = [urlTopDay, urlTopWeek, urlTopMonth]
    urlDetail = domain + '/truyen-tranh/song-tu-dao-lu-cua-toi/chap-49/238704'
    nameManga = urlDetail.split('/')[4]
    chapter = urlDetail.split('/')[5]
    print(chapter)
    # createFileJsonData()
    # arrayKinds = getListKind(driver, urlFilter)
    #getTopMangaByUrl(driver, urlTopDay)
    showDetailManga(driver, urlDetail, domain, userAgent, nameManga, chapter)
    # Đóng trình duyệt
    driver.quit()

def settings(driver, url):
    driver.get(url)# Lấy nội dung HTML của trang web
    html_content = driver.page_source
    # Sử dụng BeautifulSoup để phân tích cú pháp HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    return soup

def getListKind(driver, url):
    arr = []
    soup = settings(driver, url)
    pathParentUl = soup.find('div','right-side') #path for ul
    pathUl = pathParentUl.find_all('li')
    for li in pathUl:
        arr.append(li.a.string)

    arr.pop(0)
    return arr

def getTopMangaByUrl(driver, url):
    arr = []
    soup = settings(driver, url)
    pathParentListImages = soup.find('div', 'center-side')
    pathListImages = pathParentListImages.find_all('div', 'item')

    for path in pathListImages:
        pathUlChapter = path.find('ul', 'comic-item')
        chapter = pathUlChapter.find('li').a.string
        chapterDate = pathUlChapter.find('li').i.string
        ob = {
            'name' : path.find('h3').a.string,
            'image' : path.find('img')['data-original'],
            'pathA' : path.find('a')['href'],
            'chapter': chapter,
            'chapterDate': chapterDate

        }
        arr.append(ob)

    return arr

#Xem chi tiết manga
def showDetailManga(driver, url, domain, userAgent, nameManga, chapter):
    arr = []
    soup = settings(driver, url)
    pathParentListImages = soup.find('div','reading-detail')
    pathListImages = pathParentListImages.find_all('div', 'page-chapter')
    randomNumber = 0
    if(nameManga != ''):
        checkFolderAndCreateNew('images/' + nameManga)
        if(chapter != ''):
            randomNumber = chapter
            checkFolderAndCreateNew('images/' + nameManga + '/' + randomNumber)
        else:
            randomNumber = random.random(0, 10000)
            checkFolderAndCreateNew('images/' + nameManga + '/' + randomNumber)
    else:
        print('re-check')
        
    for path in pathListImages:
        imageUrl = path.find('img')['data-original']
        saveImageFromCloudflare(imageUrl, domain, userAgent, nameManga, randomNumber)
        arr.append(imageUrl)

    return arr


def saveImageFromCloudflare(imageUrl, domain, userAgent, nameManga, chapter):
    splitData = imageUrl.split('/')
    pathCloudflare = splitData[2]
    splitData2 = imageUrl.split('?')
    imageName = splitData2[0].split('/')[7]
    pathGetImage = splitData2[0]
    headers = {
        'authority': pathCloudflare,
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'referer': domain,
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': userAgent,
    }

    params = {
        'data': 'net',
    }
    response = requests.get('https:' + pathGetImage, params=params, headers=headers)
    print(imageName)
    with open('images/' + nameManga + '/' + chapter + '/'+imageName, "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    main()
    

    