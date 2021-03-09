from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

# Create your views here.
class Login(forms.Form):
    Username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))

class Signup(forms.Form):
    f_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    l_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    Password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))


def user_dashboard(request):
    # if request.user.is_authenticated:
    return render(request, "users/dashboard.html")
    # return HttpResponse("Not authenticated")

def user_login(request):
    form = Login()
    if request.method == "POST":
        login_form = Login(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['Username']
            password = login_form.cleaned_data['Password']
            # user = authenticate(username=username, password=password)
            # user = User.objects.all()
            # group = Group.objects.get(name="customers")
            # user_in_group = Group.objects.all()
            check_user = User.objects.filter(groups__name="customers")
            print(check_user)
            qw = check_user.first()
            if check_user is not None:
                for i in check_user:
                    i = str(i)
                    if username == i:
                        user = authenticate(username=username, password=password)
                        if user is not None:
                            return HttpResponse("Logged in as customer")
                        return HttpResponse("Error")
                return HttpResponse("Not a customer")
            return HttpResponse("Login failed")
    context = {
        "form" : form
    }
    return render(request, "users/login.html", context)

def user_signup(request):
    form = Signup()
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            username = form.cleaned_data['username']
            Email = form.cleaned_data['Email']
            Password = form.cleaned_data['Password']
            user = User.objects.create_user( username, Email, Password)
            user.first_name = f_name
            user.last_name = l_name
            group = Group.objects.get(name='customers')
            user.groups.add(group)
            user.save()
            return HttpResponse("Registered!!")
        return HttpResponse("Nooo")
    context = {
        "form" : form
    }
    return render(request, "users/signup.html", context)




