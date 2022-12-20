from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.




class Person(models.Model):
    image = models.ImageField(upload_to='person/')
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    mail = models.CharField(max_length=150)
    telegram = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body = RichTextField()

    def __str__(self):
        return str(self.name)