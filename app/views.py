from django.shortcuts import render, redirect

from .forms import ParseForm

from .sub_app import saiman_parse


def home(request):

    list = [
        {
            'name': '«Орман» СО-Э711',
            'text': 'Статический счетчик.',
            'price': '5 900 ₸',
            'price_min': '5 850 ₸',
            'img': 'CC.jpg'
        },
        {
            'name': '«Орман» СО-Э711',
            'text': 'Статический счетчик.',
            'price': '2 900 ₸',
            'price_min': '2 850 ₸',
            'img': 'CE.jpg'
        },
        {
            'name': '«Орман» СО-Э711',
            'text': 'Статический счетчик.',
            'price': '18 200 ₸',
            'price_min': '18 100 ₸',
            'img': 'CL.jpg'
        },
        {
            'name': '«Орман» СО-Э711 PLC',
            'text': 'Статический счетчик.',
            'price': '22 000 ₸',
            'price_min': '21 900 ₸',
            'img': 'CU.jpg'
        },
        {
            'name': '«Орман» Т1 СО-Э711',
            'text': 'Статический счетчик.',
            'price': '2 900 ₸',
            'price_min': '2 850 ₸',
            'img': 'CV.jpg'
        },
        {
            'name': '«Дала» СА4-Э720',
            'text': 'Счетчик прямого включения.',
            'price': '10 400 ₸',
            'price_min': '10 350 ₸',
            'img': 'NA.jpg'
        },
        {
            'name': '«Дала» СА4-Э720 Т1',
            'text': 'Счетчик прямого включения.',
            'price': '11 600 ₸',
            'price_min': '11 550 ₸',
            'img': 'NB.jpg'
        },
        {
            'name': '«Дала» СА4-Э720 ТХ',
            'text': 'Счетчик прямого включения.',
            'price': '13 600 ₸',
            'price_min': '13 550 ₸',
            'img': 'NC.jpg'
        },
        {
            'name': '«Дала» СА4У-Э720',
            'text': 'Счетчик трансформаторного включения.',
            'price': '9 400 ₸',
            'price_min': '9 350 ₸',
            'img': 'ND.jpg'
        },
        {
            'name': '«Дала» СА4У-Э720 Т1',
            'text': 'Счетчик трансформаторного включения.',
            'price': '11 200 ₸',
            'price_min': '11 150 ₸',
            'img': 'NE.jpg'
        },
        {
            'name': '«Дала» СА4У-Э720 ТХ',
            'text': 'Счетчик трансформаторного включения.',
            'price': '12 900 ₸',
            'price_min': '12 850 ₸',
            'img': 'NF.jpg'
        },
        {
            'name': '«Дала» TX P PLC IP П RS',
            'text': 'Электронный счетчик.',
            'price': '42 000 ₸',
            'price_min': '41 800 ₸',
            'img': 'NL.jpg'
        },
        {
            'name': '«Дала» СА3У-Э720',
            'text': 'Счетчик трансформаторного включения.',
            'price': '9 700 ₸',
            'price_min': '9 650 ₸',
            'img': 'NM.jpg'
        },
        {
            'name': '«Дала» СА4-Э720',
            'text': 'Счетчик прямого включения.',
            'price': '14 000 ₸',
            'price_min': '13 950 ₸',
            'img': 'NX.jpg'
        },
        {
            'name': '«Дала» СА4-Э720 ТХ',
            'text': 'Счетчик прямого включения.',
            'price': '18 400 ₸',
            'price_min': '18 350 ₸',
            'img': 'NY.jpg'
        },
    ]
    title_list = ['«Орман»',
                  '«Дала»',
                  ]

    context = {'list': list,
               'title_list': title_list,
               }
    return render(request, 'app/home.html', context)


def index(request):
    context = {}
    return render(request, 'app/index.html', context)


def column(request):
    context = {}
    return render(request, 'app/column.html', context)


def group(request):
    context = {}
    return render(request, 'app/group.html', context)


def product(request, name):
    context = {'name': name}
    return render(request, 'app/product.html', context)


def parser(request):
    if request.method == 'POST':
        parser = saiman_parse
        if parser.runnable:
            result = parser.start_parse()
            if result is not None and result != []:
                context = {'data': result}
                return render(request, 'app/saiman_data.html', context)

    form = ParseForm()
    context = {'form': form}

    return render(request, 'app/parser.html', context)
