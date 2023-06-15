import datetime

def getDetailAdidasProduct(soup):
    print('oke')
    name_product = soup.find('h1',{"class": "test-itemTitle"}).string
    # sex_product = soup.find('h2',{"data-test": "product-sub-title"}).string
    price_product = soup.find('div',{"class": "test-articlePrice"}).string
    # tax_product = soup.find('div',{"data-test": "tax-included"}).string
    # sale_product = soup.find('div',{"data-test": "product-price-reduced"}).string
    box_style_product = soup.find('li', {"class": "test-articleId"})
    style_product = box_style_product.find('span', {"class": "test-itemComment-article"}).string
    made_product = soup.find('li', {"class": "test-itemCountry"}).string
    # add_to_cart_form = soup.find('form', 'add-to-cart-form')
    # list_size = add_to_cart_form.find_all('input',{'name': 'skuAndSize'})
    box_images = soup.find('img', {'class': 'test-magnify_image_wrapper'})['src']
    # src_image = box_images.find('source')['srcset']
    created_time = datetime.datetime.now()
    modify_time = datetime.datetime.now()
    
    return {
        'name_product': name_product,
        # 'sex_product': sex_product,
        # 'price_product': convertToPrice(price_product),
        # 'tax_product': tax_product,
        # 'sale_product': sale_product,
        'style_product': style_product,
        'box_images': 'https://shop.adidas.jp' + box_images,
        # 'src_image': src_image,
        'created_time': created_time,
        'modify_time': modify_time
    }