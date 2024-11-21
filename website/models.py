from django.db import models


class Post(models.Model):
    name = models.CharField('Name', max_length=100)
    count = models.IntegerField(default=0, null=False, blank=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.name
# Create your models here.
