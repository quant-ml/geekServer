from django.shortcuts import render

def index(request):
    context = {'title': 'geekShop'}
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {'title': 'geekShop - catalogue'}
    return render(request, 'mainapp/products.html', context)

def test_context(request):
    context = {
        'title': 'geekShop',
        'header': 'welcome!',
        'username': 'ivan ivanov',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00'},
        ],
        'products_of_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00'},
        ]
    }

    return render(request, 'mainapp/test-context.html', context)