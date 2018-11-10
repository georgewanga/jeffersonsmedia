from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render,  redirect
from accounts.forms import LoginForm, RegisterForm, GuestForm
from django.utils.http import is_safe_url


def guestLoginView(request):
    form = GuestForm(request.POST or None)
    context = {
        'form':form,
    }
    content_type = None
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            pass
    return render(request, 'accounts/login.html',context,content_type)


def loginPage(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form,
    }
    content_type = None
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            pass
    return render(request, 'accounts/login.html',context,content_type)


User = get_user_model()
def registerPage(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form,
    }
    content_type = None
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username,email,password)
    return render(request, 'accounts/register.html',context,content_type)
