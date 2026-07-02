from django.shortcuts import render

def index(request):
    return render(request, "home/index.html")

def index2(request):
    return render(request, "home/index2.html")

def about(request):
    return render(request, "home/about.html")

def faq(request):
    return render(request, "home/faq.html")

def error_404(request):
    return render(request, "home/404.html")

def pricing(request):
    return render(request, "home/pricing.html")