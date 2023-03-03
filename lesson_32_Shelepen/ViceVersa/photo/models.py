from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='image/')