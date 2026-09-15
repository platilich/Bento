from django.db import models



# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=300, blank=False)

    photo = models.ImageField(upload_to='static/img/', blank=False)

    icon = models.ImageField(upload_to='static/img/', verbose_name='Site icon', blank=True)

    custom_cursor = models.BooleanField(default=True, verbose_name='Beautiful cursor')



    hide = models.BooleanField(default=False, verbose_name='Hide profile (if something goes wrong, you can hide profile)')


    class Meta:
        verbose_name = 'Profile'


    def __str__(self):
        return self.name



class Buttons(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Name')
    url = models.CharField(max_length=3000, blank=False, verbose_name='Link')

    hide = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Link'


    def __str__(self):
        return self.title