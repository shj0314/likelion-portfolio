from django.db import models

# Create your models here.


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    img = models.ImageField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
