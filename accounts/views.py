from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from result.models import Result
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User


def profile(request):
    user = request.user
    print("USER 18 ", user)
    result_history = Result.objects.filter(user=user)
    progress = Result.objects.filter(user=user).last()
    print("PROG-> ", progress)
    return render(
        request, "profile.html", {"result": result_history, "progress": progress}
    )


def register(request):
    if request.method == "POST":
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            # print("User -> ", user.is_active)
            user.is_active = False
            user.save()
            print("User -> ", user.is_active)
            token = default_token_generator.make_token(user)
            print("Token -> ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("UID -> ", uid)
            confirm_link = f"http://127.0.0.1:8000/authorizaion/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string(
                "confirm_email.html", {"confirm_link": confirm_link}
            )
            email = EmailMultiAlternatives(email_subject, "", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return redirect("register")

    else:
        register_form = forms.RegistrationForm()
    return render(
        request, "authentication.html", {"form": register_form, "type": "Registration"}
    )


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except User.DoesNotExist:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("profile")
    else:
        return redirect("homepage")


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_pass = form.cleaned_data["password"]
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
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
