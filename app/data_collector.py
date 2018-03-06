from .sub_app import saiman_parse
from .models import Company, Category, Product

import requests
from PIL import Image

from random import choice


def main():
    start_collect()


TESTPARSE = False


def start_test_collect():
    com = get_company_object('Saiman')
    cat = get_category_object('Counter')

    url = 'https://alser.kz/media/product/7200939/smartfon-samsung-galaxy-j7-2017-16-gb-chjornyj.jpg'
    image_path = save_image(url)
    Product(
        name='Смартфон Samsung Galaxy J7 2017 16 Гб, чёрный',
        description='Стиль, дополняющий функциональность. Новый Samsung Galaxy J7 создан с вниманием к мельчайшим деталям. Цельнометаллический корпус с утопленным объективом камеры идеально лежит в руке, а стекло 2.5D надежно защищает FHD-экран диагональю 5,5 дюйма от царапин и потертостей. Жизнь в каждом кадре Задняя камера смартфона с разрешением 13 мегапикселей и диафрагмой F/1.7 снимает четкие подробные фото даже при недостаточном освещении, а ее интуитивный интерфейс позволяет делать снимки одной рукой благодаря плавающей кнопке спуска — вы можете менять позу и компоновку кадра прямо в процессе съемки. Отличные портреты в любых условиях Samsung Galaxy J7 позволяет делать живые, яркие и правдоподобные автопортреты в любой ситуации, даже при недостаточном освещении, благодаря фронтальной светодиодной вспышке и вспышке для селфи. А управлять спуском можно дистанционно при помощи простого жеста. Надежная защита личных данных Samsung Galaxy J7 оснащен сканером отпечатков пальца для защиты ваших личных данных. Этот способ аутентификации можно также использовать для совершения мобильных платежей и входа в учетные записи для обеспечения максимальной защиты.',
        description_short='Samsung Galaxy J7 – это пример того, когда стиль находится в гармонии с функциональностью.',
        price='109 900',
        price_opt='109 900',
        image=image_path,
        company=com,
        category=cat,
        article=get_article(com.id, cat.id)
    ).save()


def start_collect():
    if TESTPARSE:
        start_test_collect()
        return

    parser = saiman_parse
    if parser.runnable:
        data = parser.start_parse()
        for target in data:
            collect(target)


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
            description_short=d['description_short'],
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


import os


def save_image(url):
    image_name = 'app/images/product/{}'.format(get_name())

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    saveplace = '{}/app/static/{}'.format(BASE_DIR, image_name)

    response = requests.get(url, stream=True)
    response.raw.decode_content = True

    img = Image.open(response.raw)
    img.save(saveplace, "PNG")

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
