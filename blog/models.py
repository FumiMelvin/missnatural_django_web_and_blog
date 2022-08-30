from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    intro = models.TextField()
    body = RichTextField()
    image = models.ImageField(upload_to='images/blog/', null = True, blank = True)
    date_published = models.DateTimeField(auto_now_add=True)

class Meta():
    ordering = ['-date_published']