from django.shortcuts import render

from .models import Category, Product

# Create your views here.
def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {

        'categories': categories,
        'products' : products,
    }

    return render(request, 'catalog/main.html', context)

def product_view(request, product_slug):
    product = Product.objects.get(slug = product_slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories,
    }
    return render(request,  'catalog/product.html', context)


def category_view(request, category_slug):
    category = Category.objects.get(slug = category_slug)
    categories = Category.objects.all()
    products_of_category = Product.objects.filter(category = category)

    context = {
        'category': category,
        'products_of_category':products_of_category,
        'categories': categories,
    }
    return render(request, 'catalog/category.html', context)
