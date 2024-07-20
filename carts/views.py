from django.shortcuts import render, redirect
from store.models import product
from .models import cart, cartItem
# Create your views here.

def _cart_id(request):
    carts = request.session.session_key

    if not carts:
        carts = request.session.create()
    

def add_cart(request, id):
    products = product.objects.get(id=id)

    try:
        carts = cart.objects.get(cart_id = _cart_id(request))

    except cart.DoesNotExist:
        carts = cart.objects.create(
            cart_id = _cart_id(request)
        )
    carts.save()
    

    try:
        cart_item = cartItem.objects.get(product = products, cart = carts)
        cart_item.quatity += 1
        cart_item.save()

    except cartItem.DoesNotExist:
        cart_item = cartItem.objects.create(
            product = products,
            quatity = 1,
            cart = carts,

        )
        cart_item.save()
    return redirect('cart')



def cart(request):
    return render(request, 'store/cart.html')