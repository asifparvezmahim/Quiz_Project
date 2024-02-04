from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from result.models import Result
from quiz_taken.models import Quiz_Taken


def profile(request):
    result_history = Result.objects.filter(user=request.user)
    progress = Result.objects.filter(user=request.user).last()
    print("PROG-> ", progress)
    return render(
        request, "profile.html", {"result": result_history, "progress": progress}
    )


def register(request):
    if request.method == "POST":
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect("register")

    else:
        register_form = forms.RegistrationForm()
    return render(
        request, "authentication.html", {"form": register_form, "type": "Registration"}
    )


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_pass = form.cleaned_data["password"]
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                print("Normal uSER")
                login(request, user)
                return redirect("profile")

            else:
                return redirect("register")
    else:
        form = AuthenticationForm()
        return render(request, "authentication.html", {"form": form, "type": "Login"})


def user_logout(request):
    logout(request)
    return redirect("user_login")
