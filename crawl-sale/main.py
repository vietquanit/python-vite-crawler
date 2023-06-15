from ultis import settingDriver, openBrowser, closeBrowser, quitBrowser
from crawl.nike import getDetailProduct
from crawl.adidas import getDetailAdidasProduct
from crawl.rakuten import getDetailRakutenProduct

def main():
    # url = 'https://www.nike.com/jp/t/ナイキ-ダンク-low-se-ウィメンズシューズ-KzTs4C/DV1160-100'
    # url = 'https://shop.adidas.jp/products/EF1730/'
    url = 'https://item.rakuten.co.jp/nike-official/cj0882-400/'
    driver = settingDriver()
    soup = openBrowser(driver, url)
    # brand = 'Nike'
    # brand = 'Adidas'
    brand = 'Rakuten'
    if brand == 'Nike':
        data = getDetailProduct(soup)
        print(data)
    elif brand == 'Adidas':
        data = getDetailAdidasProduct(soup)
        print(data)
    else:
        data = getDetailRakutenProduct(soup)
        print(data)

    #quit browser
    quitBrowser(driver)

if __name__ == "__main__":
    main()
    

    