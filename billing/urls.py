from django.urls import path
from accounts.views import (
    loginPage,
    registerPage)


app_name = 'billing'


urlpatterns = [
    path('login/', loginPage, name='usr_login'),
    path('register/', registerPage, name='usr_registration'),
]
