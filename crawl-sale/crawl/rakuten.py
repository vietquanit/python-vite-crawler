import datetime

def getDetailRakutenProduct(soup):
    box_name_product = soup.find('span',{"class": "normal_reserve_item_name"})
    name_product = box_name_product.find_all('b')
    # sex_product = soup.find('h2',{"data-test": "product-sub-title"}).string
    td_price_product = soup.find('td',{"irc": "DualPrice"})
    price_product = td_price_product.select_one('div:nth-of-type(2)')
    # # tax_product = soup.find('div',{"data-test": "tax-included"}).string
    # sale_product = soup.find('div',{"data-test": "product-price-reduced"}).string
    # box_style_product = soup.find('li', {"class": "test-articleId"})
    # style_product = box_style_product.find('span', {"class": "test-itemComment-article"}).string
    # made_product = soup.find('li', {"class": "test-itemCountry"}).string
    # # add_to_cart_form = soup.find('form', 'add-to-cart-form')
    # # list_size = add_to_cart_form.find_all('input',{'name': 'skuAndSize'})
    # box_images = soup.find('div', {'class': 'product-top-img'})
    # src_image = box_images.find('img')['src']

    created_time = datetime.datetime.now()
    modify_time = datetime.datetime.now()
    
    return {
        'name_product': name_product[0],
        # 'sex_product': sex_product,
        'price_product': price_product,
        # 'tax_product': tax_product,
        # 'sale_product': sale_product,
        # 'style_product': style_product,
        # 'box_images': box_images,
        # 'src_image': src_image,
        'created_time': created_time,
        'modify_time': modify_time
    }