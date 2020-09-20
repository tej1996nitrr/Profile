from django.db import models

# Create your models here.
class Skills(models.Model):
    skill = models.CharField(max_length=50, unique=True)
    url = models.URLField()

class Post(models.Model):

    headline = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    body = models.TextField(null=True, blank=True)
	
    def __str__(self):
        return self.headline
