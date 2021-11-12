from django.db import models

# Create your models here.


class package(models.Model):
    aboutus = models.URLField()
    image = models.ImageField(upload_to='polls/images/')
