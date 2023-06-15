import datetime

def getDetailProduct(soup):
    name_product = soup.find('h1',{"data-test": "product-title"}).string
    sex_product = soup.find('h2',{"data-test": "product-sub-title"}).string
    price_product = soup.find('div',{"data-test": "product-price"}).string
    tax_product = soup.find('div',{"data-test": "tax-included"}).string
    sale_product = soup.find('div',{"data-test": "product-price-reduced"}).string
    style_product = soup.find('li', {"class": "description-preview__style-color"}).string
    made_product = soup.find('li', {"class": "description-preview__origin ncss-li"}).string
    # add_to_cart_form = soup.find('form', 'add-to-cart-form')
    # list_size = add_to_cart_form.find_all('input',{'name': 'skuAndSize'})
    box_images = soup.find('button', {'data-sub-type': 'image'})
    src_image = box_images.find('source')['srcset']
    created_time = datetime.datetime.now()
    modify_time = datetime.datetime.now()
    
    return {
        'name_product': name_product,
        'sex_product': sex_product,
        'price_product': convertToPrice(price_product),
        'tax_product': tax_product,
        'sale_product': sale_product,
        'style_product': style_product,
        'box_images': box_images,
        'src_image': src_image,
        'created_time': created_time,
        'modify_time': modify_time
    }

def convertToPrice(price):
    splitPrice = price.split('￥')
    markPrice = splitPrice[0]
    priceText = splitPrice[1]
    priceNumber = priceText.split(',')
    joinNumberPrice = priceNumber[0]+priceNumber[1]
    floatNumberPrice = float(joinNumberPrice)
    return int(floatNumberPrice)