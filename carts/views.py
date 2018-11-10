from django.shortcuts import render, redirect
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile
from orders.models import Order
from carts.models import Cart
from products.models import Product


def cartHome(request):
    cart_obj, new_obj = Cart.objects.newOrGet(request)
    products = cart_obj.products.all()
    context={
        'cart':cart_obj
    }
    content_type=None
    return render(request, 'carts/home.html',context, content_type)


def cartUpdate(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect('cart:home')
        cart_obj, new_obj = Cart.objects.newOrGet(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
    # return redirect(product_obj.get_absolute_url())
    return redirect('cart:home')


def checkoutHome(request):
    cart_obj, cart_created = Cart.objects.newOrGet(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect('cart:home')
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    user = request.user
    billing_profile = None
    login_form = LoginForm()
    guest_form = GuestForm()

    if user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(
            user=user, email=user.email)
    context={
        'object':order_obj,
        'billing_profile':billing_profile,
        'login_form':login_form,
    }
    content_type=None
    return render(request,'carts/checkout.html',context, content_type)