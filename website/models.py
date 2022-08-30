from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    eventDetails = RichTextField()
    poster = models.ImageField(upload_to='event/', null = True, blank = True)