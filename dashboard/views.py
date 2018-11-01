from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from dashboard import forms 

def home(request):
    context = {
        'page_title':'Dashboard'
    }
    content_type = None
    return render(request, 'dashboard/home.html',context,content_type)


def loginPage(request):
    form = forms.LoginForm(request.POST or None)
    context = {
        'page_title':'Login ',
        'form': form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        username=form.cleaned_data.get('Username')
        password=form.cleaned_data.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('/login')
        else:
            print('Error')
    content_type = None
    return render(request, 'auth/login.html',context,content_type)


User = get_user_model()
def registerPage(request):
    form = forms.RegisterForm(request.POST or None)
    context = {
        'page_title':'Register',
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        new_user = User.objects.create_user(username,email,password)
    content_type = None
    return render(request, 'auth/register.html',context,content_type)


def addProduct(request):
    form = forms.AddItemForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        'page_title':'Add Item',
        'form': form
    }
    content_type = None
    return render(request, 'dashboard/add_product.html',context,content_type)