from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        con_password = request.POST['con_password']
        if con_password == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This User Name Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already taken')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                username=username, password=password)
            user.save()
            print('user created')
        else:
            print('incorrect password')
            return redirect('register')
        return redirect('login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
