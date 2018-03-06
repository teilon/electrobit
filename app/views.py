from django.shortcuts import render, redirect
from django.views import generic
from .forms import ParseForm

from .sub_app import saiman_parse

from .models import Product, Category


class HomeIndex(generic.ListView):
    template_name = 'app/home_index.html'
    context_object_name = 'list'

    def get_queryset(self):
        # Content.objects.all().order_by('?')[:100]
        # return Product.objects.all().order_by('?')[:10]
        return Product.objects.all().order_by('?')[:10]


class CounterIndex(generic.ListView):
    template_name = 'app/home_view.html'
    context_object_name = 'list'

    def get_queryset(self):
        cat = Category.objects.get(name='Counter')
        return cat.product_set.all()


class CounterIndexWithTitle(CounterIndex):
    def get_context_data(self, **kwargs):
        context = super(CounterIndex, self).get_context_data(**kwargs)
        context['title'] = 'Счетчики'
        return context


class ProductItem(generic.DetailView):
    template_name = 'app/product.html'
    model = Product


class ProductItemWithOther(ProductItem):
    def get_context_data(self, **kwargs):
        context = super(ProductItem, self).get_context_data(**kwargs)
        current_object = context['object']
        category = Product.objects.get(id=current_object.id).category
        product_list = Product.objects.all().filter(category=category).order_by('?')[:10]
        context['list'] = product_list
        return context


class TransformatorIndex(generic.ListView):
    template_name = 'app/home_view.html'
    context_object_name = 'list'

    def get_queryset(self):
        cat = Category.objects.get(name='Transformator')
        return cat.product_set.all()


class TransformatorIndexWithTitle(TransformatorIndex):
    def get_context_data(self, **kwargs):
        context = super(TransformatorIndex, self).get_context_data(**kwargs)
        context['title'] = 'Трансформаторы'
        return context


class BoardIndex(generic.ListView):
    template_name = 'app/home_view.html'
    context_object_name = 'list'

    def get_queryset(self):
        cat = Category.objects.get(name='Board')
        return cat.product_set.all()


class BoardIndexWithTitle(BoardIndex):
    def get_context_data(self, **kwargs):
        context = super(BoardIndex, self).get_context_data(**kwargs)
        context['title'] = 'Шкафы учета'
        return context


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
    list = Product.objects.all().order_by('?')[:10]
    context = {'name': name,
               'list': list}
    return render(request, 'app/product.html', context)


# parser for 'saiman.kz'

from . import data_collector


def parser(request):
    if request.method == 'POST':
        collector = data_collector
        collector.start_collect()
        # parser = saiman_parse
        # if parser.runnable:
        #     result = parser.start_parse()
        #     if result is not None and result != []:
        #         context = {'data': result}
        #         return render(request, 'app/saiman_data.html', context)

    form = ParseForm()
    context = {'form': form}
    return render(request, 'app/parser.html', context)
