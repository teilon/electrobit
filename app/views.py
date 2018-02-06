from django.shortcuts import render, redirect


def home(request):
    context = {}
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
