from django.shortcuts import render

def home(request):
    context = {
        'page_title':'Dashboard'
    }
    content_type = None
    return render(request, 'dashboard/home.html',context,content_type)