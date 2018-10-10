from django.db import models

# Create your models here.
class Blog(models.Model):
    """docstring for ."""
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to ='images/')
