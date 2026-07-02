from django.shortcuts import render

def course(request):
    return render(request,'courses/course.html')

def course_details(request):
    return render(request, "courses/course_details.html")