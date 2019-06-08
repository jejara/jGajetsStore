from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Category, Product, Cart, CartItem

# Create your views here.
def base_view(request):
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {

        'categories': categories,
        'products' : products,
        'cart': cart,
    }

    return render(request, 'catalog/main.html', context)

def product_view(request, product_slug):
    cart = Cart.objects.first()

    product = Product.objects.get(slug = product_slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories,
        'cart': cart,

    }
    return render(request,  'catalog/product.html', context)


def category_view(request, category_slug):
    cart = Cart.objects.first()
    category = Category.objects.get(slug = category_slug)
    categories = Category.objects.all()
    products_of_category = Product.objects.filter(category = category)

    context = {
        'category': category,
        'products_of_category':products_of_category,
        'categories': categories,
        'cart': cart,
    }
    return render(request, 'catalog/category.html', context)


def cart_view(request):
    categories = Category.objects.all()

    cart = Cart.objects.first()

    context = {
        'cart': cart,
        'categories': categories,
    }
    return render(request, 'catalog/cart.html', context)


def add_to_cart_view(request, product_slug):

    product = Product.objects.get(slug=product_slug)
    new_item, _ = CartItem.objects.get_or_create(product = product, item_total = product.price)
    cart = Cart.objects.first()

    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.save()
        return HttpResponseRedirect('/cart/')


