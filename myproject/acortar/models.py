from django.db import models

# Create your models here.
class ShortedUrl(models.Model):
    urloriginal = models.TextField()
