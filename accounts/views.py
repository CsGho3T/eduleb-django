from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.contrib.auth import logout

def login_view(request):

    error = False

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

        error = True

    return render(
        request,
        "accounts/login.html",
        {
            "error": error
        }
    )


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if request.method == "POST":

            form = RegisterForm(request.POST)

            print("POST:", request.POST)
            print("VALID:", form.is_valid())
            print("ERRORS:", form.errors)

            if form.is_valid():
                user = form.save()

                print("USER SAVED:", user.username)

                return redirect("login")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )

def logout_view(request):

    logout(request)

    return redirect("home")





