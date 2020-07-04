from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_image = models.FileField(upload_to='images/', blank=True)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title
