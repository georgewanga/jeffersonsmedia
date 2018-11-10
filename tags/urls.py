from django.urls import path
from search.views import (
    SearchProductView,
) 

app_name = 'tags'

urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),
]
