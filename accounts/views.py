from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from result.models import Result
from quiz_taken.models import Quiz_Taken
from django.contrib import messages


def profile(request):
    result_history = Result.objects.filter(user=request.user)
    progress = Result.objects.filter(user=request.user).last()
    return render(
        request, "profile.html", {"result": result_history, "progress": progress}
    )


def activateEmail(request, user, to_email):
    messages.success(
        request,
        f"Dear {user}, Please Go To Your Email  {to_email} and Click Your Recieve Activation Link To Log in Your Account",
    )


def register(request):
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get("email"))
            return redirect("homepage")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

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
