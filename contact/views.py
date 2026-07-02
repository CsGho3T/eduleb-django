from django.shortcuts import render, redirect

def contact(request):
    return  render(request, "contact/contact.html")

def thankyou(request):
    return render(request, "contact/thank-you.html")

