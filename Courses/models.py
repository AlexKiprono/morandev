import os
from django.db import models


def Media(instance, filename):
    return os.path.join('media', str(instance.id), filename)

# Create your models here.
class Course(models.Model):
    
    categorychoices = (
        ('1', 'CYBER SECURITY'),
        ('2', 'ETHICAL HACKING'),
        ('3', 'FORENSICS'),
        ('4', 'SOFTWARE DEV'),
        ('5', 'WELFARE')
    )
    category = models.CharField(max_length=25, null=False,choices=categorychoices )
    title = models.CharField(max_length=50, null=False, default='')
    image = models.ImageField(upload_to=Media)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    subject = models.TextField(max_length=1200, null=False)
    
    def __str__(self):
        return self.category
    
    
    
    