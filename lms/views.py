from django.shortcuts import render, get_object_or_404
from Courses.models import Course_product
from Categories.models import Category

def index(request):
    return render(request, 'index.html')

def indexView(request, category_slug=None):
    if category_slug:
        courses = Course_product.objects.filter(category__slug=category_slug)
    else:
        courses = Course_product.objects.all()
    categories = Category.objects.all()
    context = {
        'courses': courses,
        'categories': categories,
        'category_slug': category_slug
    }
    return render(request, 'indexView.html', context)

# def detailview(request, category_slug, id):
#     try:
#         course = Course_product.objects.get(category__slug=category_slug, slug=id)
#     except Exception as e:
#         raise e
#     context = {
#         'course': course,
#     }
#     return render(request, 'detailview.html', context)


def detailview(request, category_slug, course_product_slug):
    course_product = get_object_or_404(Course_product, category__slug=category_slug, slug=course_product_slug)
    context = {
        'course_product': course_product
    }
    return render(request, 'detailview.html', context)





