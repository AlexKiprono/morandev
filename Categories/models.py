from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=False)
    
    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')
        
    def get_url(self):
        return reverse('Courses_by_Category', kwargs={'category_slug': self.slug})


    def __str__(self):
        return self.category_name
    
