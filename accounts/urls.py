from django.urls import path
from accounts.views import (
    loginPage,
    registerPage)


app_name = 'carts'


urlpatterns = [
    path('login/', loginPage, name='usr_login'),
    path('register/', registerPage, name='usr_registration'),
]
