from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username, password=password)

    if not user:
        messages.error(request, 'username or password invalid.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    if not name or not last_name or not email or not username or not password or not password2:
        messages.error(request, 'You need to fulfill all the fields')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Invalid email')
        return render(request, 'accounts/register.html')

    if len(password) < 6:
        messages.error(
            request, 'Password needs to have more than six characters')
        return render(request, 'accounts/register.html')

    if len(username) < 6:
        messages.error(
            request, 'User needs to have more than six characters')
        return render(request, 'accounts/register.html')

    if password != password2:
        messages.error(
            request, 'Passwords are not the same')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=username).exists():
        messages.error(
            request, 'Username already exists')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(
            request, 'Email already exists')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Successfully registered!')

    user = User.objects.create_user(
        username=username, email=email, password=password, first_name=name, last_name=last_name)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
