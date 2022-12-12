from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(unique= True, max_length=25)
    password = models.TextField()
    name = models.TextField()
    email = models.EmailField()


class Project(models.Model):
    photo = models.TextField()
    title = models.TextField()
    description = models.TextField()
    tags = models.TextField()
    url_github = models.TextField()
    user = models.ForeignKey(User, null= False, on_delete=models.CASCADE)