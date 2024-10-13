from django.shortcuts import render, redirect
from userpanel.forms import RegistrationForm, LoginForm, ProfileForm, BlogForm, CommentForm
from django.contrib import messages
from adminpanel.models import Profile,Blog,Comment
from django.contrib.auth import authenticate,login


# Create your views here.
def Home(request):
    blogs = Blog.objects.all()
    return render(request,'sitevisitor/home.html',{'blogs': blogs})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                messages.success(request,f'Login Successfull as - {user}')
                return redirect('userpanel:user_home')
            else:
                messages.error(request,'Invalid Username or Password!!')
                return redirect('sitevisitor:login')
    
    else:
        form = LoginForm()
    return render(request,'sitevisitor/login.html',{'form':form})

def Registration(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST, request.FILES)
        profile_form = ProfileForm(request.POST, request.FILES)
        if reg_form.is_valid() and profile_form.is_valid():
            user = reg_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request,'Successfully Registered')
            return redirect('sitevisitor:home')
        
        else:
            messages.error(request,'Registration failed. Please try again.')
            return redirect('sitevisitor:registration')
    else:
        reg_form = RegistrationForm()
        profile_form = ProfileForm()
    return render(request,'sitevisitor/registration.html',{'reg_form':reg_form, 'profile_form':profile_form})

def Forgot_Password(request):
    return render(request,'sitevisitor/forgot_password.html')

def Reset_Password(request):
    return render(request,'sitevisitor/reset_password.html')

def otp(request):
    return render(request,'sitevisitor/otp.html')


def error_page(request):
    return render(request, 'sitevisitor/404.html')