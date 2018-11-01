from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', views.loginPage, name='usr_login'),
    path('register/', views.registerPage, name='usr_registration'),
    path('addproduct/', views.addProduct, name='prod_registration'),
    path('', views.home, name='home'),
]
