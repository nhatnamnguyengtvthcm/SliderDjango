from django.db import models

# Create your models here.

class Slider(models.Model):
    slider_img = models.ImageField()
    created_on = models.DateTimeField(auto_now_add = True, null = True, blank = True)
    updated_on = models.DateTimeField(auto_now = True, null = True, blank = True)
