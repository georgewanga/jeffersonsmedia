from django.urls import path
from carts.views import (
    cartHome,
    cartUpdate,
    checkoutHome
) 

app_name = 'carts'

urlpatterns = [
    path('', cartHome, name='home'),
    path('update/', cartUpdate, name='update'),
    path('checkout/', checkoutHome, name='checkout'),
]
