from django.db import models

class Resipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.TextField()

    def __str__(self):
        return self.username