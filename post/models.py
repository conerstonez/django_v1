from django.db import models
from django.urls import reverse


# Create your models here.


class Author(models.Model):
    username = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
