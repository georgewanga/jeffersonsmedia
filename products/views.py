from django.shortcuts import render

def home(request):
    context = {
        'page_title':'Products'
    }
    content_type = None
    return render(request, 'products/home.html',context,content_type)