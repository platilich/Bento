from django.db import models

# Create your models here.
class Page(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=300, blank=False)

    photo = models.ImageField(upload_to='static/img/' ,blank=False)


    def __str__(self):
        return self.name



class Buttons(models.Model):
    title = models.CharField(max_length=100, blank=False)
    url = models.CharField(max_length=3000, blank=False)


    def __str__(self):
        return self.title