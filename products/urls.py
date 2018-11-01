from django.urls import path
from products.views import (
    ProductListView,
    ProductDetailSlugView,
    # home,
    # product_list_view,
    # ProductFeaturedListView,
    # product_detail_view,
    # ProductDetailView,
    # ProductFeaturedDetailView
) 

app_name = 'products'

urlpatterns = [
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    path('', ProductListView.as_view(), name='list'),
    # path('products/', ProductListView.as_view(), name='products'),
    # path('', home, name='home_page'),
    # path('products_fbv/', product_list_view, name='products_fbv'),
    # path('featured/', ProductFeaturedListView.as_view(), name='featured'),
    # path('products_fbv/<int:pk>/', product_detail_view, name='product_detail_fbv'),
    # # path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('featured/<int:pk>/', ProductFeaturedDetailView.as_view(), name='featured_detail')
]
