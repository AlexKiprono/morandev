from django.shortcuts import render, get_object_or_404
from Courses.models import Course

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def detail_view(request, pk):
    courses = Course.objects.get(pk=pk)
    return render(request, 'view.html', {'courses': courses})

















# def detail_view(request, pk):
#     course = Course.objects.filter(pk=pk)
#     return render(request, 'view.html', {'course': course})




