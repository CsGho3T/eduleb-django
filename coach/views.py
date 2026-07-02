from django.shortcuts import render

def instructer(request):
    return render(request, "coach/instructor.html")

def ins_details(request):
    return render(request, "coach/ins_details.html")