import os
from django.db import models
from django.urls import reverse
from Categories.models import Category
from django.template.defaultfilters import slugify


def Media(instance, filename):
    return os.path.join('media', str(instance.id), filename)


class Course_product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50, null=False, default='')
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='photos/courses')
    subject = models.TextField(max_length=2000, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super(Course_product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detailview', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.course_name


