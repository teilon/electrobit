from .sub_app import saiman_parse
from .models import Company, Category, Product

import requests
from PIL import Image

from random import choice


def main():
    start_collect()


def start_collect():
    # test()
    parser = saiman_parse
    if parser.runnable:
        data = parser.start_parse()
        # for target in data:
        #     collect(target)


def collect(data):
    com = get_company_object(data['company'])
    cat = get_category_object(data['category'])

    for d in data['items']:

        if Product.objects.filter(name=d['name']):
            continue

        url = d['img_source']
        image_path = save_image(url)
        Product(
            name=d['name'],
            description=d['description'],
            description_short=d['description'],
            price=d['cost'],
            price_opt=d['cost'],
            image=image_path,
            company=com,
            category=cat,
            article=get_article(com.id, cat.id)
        ).save()


def get_company_object(company_name):
    if not Company.objects.filter(name=company_name):
        Company(
            name=company_name
        ).save()
    return Company.objects.get(name=company_name)


def get_category_object(category_name):
    if not Category.objects.filter(name=category_name):
        Category(
            name=category_name
        ).save()
    return Category.objects.get(name=category_name)


def save_image(url):
    image_name = 'app/images/product/{}'.format(get_name())

    response = requests.get(url, stream=True)
    response.raw.decode_content = True

    img = Image.open(response.raw)
    img.save(image_name, "PNG")

    return image_name


def get_article(company_id, category_id):
    com = str(company_id)
    cat = str(category_id)
    return int('{:0>3}{:0>3}'.format(com[-3:], cat[-3:]))


def get_name():
    name = ''
    for n in range(16):
        name += chr(choice(range(ord('a'), ord('z') + 1)))

    return name


def test():
    p = Product.objects.filter(name='name')
    if p == []:
        print('not None')
        return
    print('None')
