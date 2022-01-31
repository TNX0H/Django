from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index1.html')


def contact(request):
    return render(request, 'mainapp/contact1.html')


links_menu = [
    {
        'url': 'products',
        'title': 'Все'
    },
    {
        'url': 'products_home',
        'title': 'Дом'
    },
    {
        'url': 'products_offices',
        'title': 'Офис'
    },
    {
        'url': 'products_modern',
        'title': 'Модерн'
    },
    {
        'url': 'products_classic',
        'title': 'Классика'
    },
]


def products(request):
    context = {
        'links_menu': links_menu
    }

    return render(request, 'mainapp/products1.html')


def products_home(request):
    context = {
        'links_menu': links_menu
    }

    return render(request, 'mainapp/products1.html')


def products_offices(request):
    context = {
        'links_menu': links_menu
    }

    return render(request, 'mainapp/products1.html')


def products_modern(request):
    context = {
        'links_menu': links_menu
    }

    return render(request, 'mainapp/products1.html')


def products_classic(request):
    context = {
        'links_menu': links_menu
    }

    return render(request, 'mainapp/products1.html')
