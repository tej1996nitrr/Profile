from django.db import models

# Create your models here.
class Skills(models.Model):
    skill = models.CharField(max_length=50, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.skill

class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name
class Post(models.Model):

    headline = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    body = models.TextField(null=True, blank=True)
    url = models.URLField(default="https://google.com")
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    github = models.URLField(default="https://google.com")

	
    def __str__(self):
        return self.headline
